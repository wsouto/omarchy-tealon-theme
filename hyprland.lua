local active_border_color = "#24C4D3"
local inactive_border_color = "rgba(595959aa)"

hl.config({
  general = {
    col = {
      active_border = active_border_color,
      inactive_border = inactive_border_color,
    },
  },

  group = {
    col = {
      border_active = active_border_color,
      border_inactive = inactive_border_color,
    },
  },
})

-- Terminals 5% more transparent than Omarchy's default 0.985/0.96 opacity.
o.window({ tag = "terminal" }, { opacity = "0.935 0.91" })
