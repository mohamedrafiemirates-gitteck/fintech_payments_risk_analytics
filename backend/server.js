const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");
const { createClient } = require("@supabase/supabase-js");

dotenv.config();

const app = express();

app.use(cors());
app.use(express.json());
app.set("trust proxy", true);

const PORT = process.env.PORT || 3000;
const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_SERVICE_ROLE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

if (!SUPABASE_URL || !SUPABASE_SERVICE_ROLE_KEY) {
  throw new Error("Missing Supabase environment variables");
}

const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY);

function getClientIp(req) {
  const forwardedFor = req.headers["x-forwarded-for"];

  if (forwardedFor) {
    return forwardedFor.split(",")[0].trim();
  }

  return req.ip || req.socket.remoteAddress || null;
}

async function getIpDetails(ipAddress) {
  if (!ipAddress) {
    return {
      ip_country: null,
      ip_city: null
    };
  }

  try {
    const response = await fetch(`https://ipwho.is/${ipAddress}`);
    const data = await response.json();

    if (!data.success) {
      return {
        ip_country: null,
        ip_city: null
      };
    }

    return {
      ip_country: data.country || null,
      ip_city: data.city || null
    };
  } catch (error) {
    return {
      ip_country: null,
      ip_city: null
    };
  }
}

app.get("/health", (req, res) => {
  res.json({
    status: "ok",
    service: "fintech-device-session-api"
  });
});

app.post("/capture-device-session", async (req, res) => {
  try {
    const payload = req.body;

    if (!payload.customer_id) {
      return res.status(400).json({
        error: "customer_id is required"
      });
    }

    const ipAddress = getClientIp(req);
    const ipDetails = await getIpDetails(ipAddress);

    const sessionId = "DEV" + Date.now() + Math.floor(Math.random() * 1000);

    const record = {
      device_session_id: sessionId,
      customer_id: payload.customer_id,
      device_id: payload.device_id,
      device_type: payload.device_type,
      os_name: payload.os_name,
      browser_name: payload.browser_name,
      app_version: payload.app_version || "backend-test-v1",
      ip_address: ipAddress,
      ip_country: ipDetails.ip_country,
      ip_city: ipDetails.ip_city,
      location_emirate: payload.location_emirate,
      latitude: payload.latitude,
      longitude: payload.longitude,
      location_address: payload.location_address,
      gps_accuracy_meters: payload.gps_accuracy_meters,
      network_type: payload.network_type,
      is_vpn: false,
      is_proxy: false,
      login_timestamp: new Date().toISOString(),
      session_status: "Active"
    };

    const { data, error } = await supabase
      .from("customer_device_sessions")
      .insert(record)
      .select();

    if (error) {
      return res.status(400).json({
        error: error.message,
        details: error
      });
    }

    return res.status(201).json({
      message: "Device session captured successfully",
      device_session_id: sessionId,
      data
    });
  } catch (error) {
    return res.status(500).json({
      error: String(error)
    });
  }
});

app.listen(PORT, () => {
  console.log(`Device session API running on http://localhost:${PORT}`);
});