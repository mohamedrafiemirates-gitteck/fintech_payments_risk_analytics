import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from "https://esm.sh/@supabase/supabase-js@2"

serve(async (req) => {
  try {
    if (req.method !== "POST") {
      return new Response(
        JSON.stringify({ error: "Only POST requests are allowed" }),
        { status: 405, headers: { "Content-Type": "application/json" } }
      )
    }

    const supabaseUrl = Deno.env.get("SUPABASE_URL")
    const serviceRoleKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")

    if (!supabaseUrl || !serviceRoleKey) {
      return new Response(
        JSON.stringify({ error: "Server environment variables are missing" }),
        { status: 500, headers: { "Content-Type": "application/json" } }
      )
    }

    const supabase = createClient(supabaseUrl, serviceRoleKey)

    const payload = await req.json()

    const authHeader = req.headers.get("Authorization")
    if (!authHeader) {
      return new Response(
        JSON.stringify({ error: "Missing Authorization header" }),
        { status: 401, headers: { "Content-Type": "application/json" } }
      )
    }

    const userClient = createClient(supabaseUrl, Deno.env.get("SUPABASE_ANON_KEY")!, {
      global: {
        headers: {
          Authorization: authHeader,
        },
      },
    })

    const {
      data: { user },
      error: userError,
    } = await userClient.auth.getUser()

    if (userError || !user) {
      return new Response(
        JSON.stringify({ error: "Invalid or expired user session" }),
        { status: 401, headers: { "Content-Type": "application/json" } }
      )
    }

    const ipAddress =
      req.headers.get("x-forwarded-for")?.split(",")[0]?.trim() ||
      req.headers.get("cf-connecting-ip") ||
      req.headers.get("x-real-ip") ||
      null

    const sessionId = `DEV${Date.now()}`

    const record = {
      device_session_id: sessionId,
      customer_id: payload.customer_id,
      device_id: payload.device_id,
      device_type: payload.device_type,
      os_name: payload.os_name,
      browser_name: payload.browser_name,
      app_version: payload.app_version,
      ip_address: ipAddress,
      ip_country: payload.ip_country,
      ip_city: payload.ip_city,
      location_emirate: payload.location_emirate,
      latitude: payload.latitude,
      longitude: payload.longitude,
      location_address: payload.location_address,
      gps_accuracy_meters: payload.gps_accuracy_meters,
      network_type: payload.network_type,
      is_vpn: payload.is_vpn ?? false,
      is_proxy: payload.is_proxy ?? false,
      login_timestamp: new Date().toISOString(),
      session_status: "Active",
    }

    const { data, error } = await supabase
      .from("customer_device_sessions")
      .insert(record)
      .select()

    if (error) {
      return new Response(
        JSON.stringify({ error: error.message }),
        { status: 400, headers: { "Content-Type": "application/json" } }
      )
    }

    return new Response(
      JSON.stringify({
        message: "Device session captured successfully",
        device_session_id: sessionId,
        data,
      }),
      { status: 200, headers: { "Content-Type": "application/json" } }
    )
  } catch (error) {
    return new Response(
      JSON.stringify({ error: String(error) }),
      { status: 500, headers: { "Content-Type": "application/json" } }
    )
  }
})