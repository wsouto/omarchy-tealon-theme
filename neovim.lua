--
--
--                   @@@        @@@          @@                      @@         @@@        @@@
--            @@@@          @@             @@                          @@            @@         @@@@
--          @@@           @@              @@                            @@             @@          @@@
--        @@@            @@               @@                            @@              @@           @@@
--       @@                                                                                            @@
--      @@                                                                                              @@
--    @              @@           @@         @@  @@  @@@  @@@ @@  @@@@      @@@@ @@    @@@@ @@             @
--    @@                                                                                                  @@
--     @@                                                                                                @@
--      @@              @@                @@                            @@                @@            @@
--        @@             @@               @@                            @@               @@           @@
--          @@            @@               @@                          @@               @@          @@
--               @@@         @@@            @@                        @@            @@         @@@
--                  @@@         @@           @@                      @@          @@@        @@@
--
--                                          ＵＮＩＴＥＤ ＩＮ 𝙎𝙀𝙑𝙀𝙍𝘼𝙉𝘾𝙀

return {
	{
		"bjarneo/aether.nvim",
		branch = "v2",
		name = "aether",
		priority = 1000,
		opts = {
			transparent = false,
			colors = {
				-- Background colors
				bg = "#081B24",
				bg_dark = "#081B24",
				bg_highlight = "#103848",

				-- Foreground colors
				-- fg: Object properties, builtin types, builtin variables, member access, default text
				fg = "#D6E7E8",
				-- fg_dark: Inactive elements, statusline, secondary text
				fg_dark = "#D6E7E8",
				-- comment: Line highlight, gutter elements, disabled states
				comment = "#103848",

				-- Accent colors
				-- red: Errors, diagnostics, tags, deletions, breakpoints
				red = "#158CA3",
				-- orange: Constants, numbers, current line number, git modifications
				orange = "#24C4D3",
				-- yellow: Types, classes, constructors, warnings, numbers, booleans
				yellow = "#196075",
				-- green: Comments, strings, success states, git additions
				green = "#13738C",
				-- cyan: Parameters, regex, preprocessor, hints, properties
				cyan = "#72E2EA",
				-- blue: Functions, keywords, directories, links, info diagnostics
				blue = "#24C4D3",
				-- purple: Storage keywords, special keywords, identifiers, namespaces
				purple = "#D2A5A8",
				-- magenta: Function declarations, exception handling, tags
				magenta = "#72E2EA",
			},
		},
		config = function(_, opts)
			require("aether").setup(opts)
			vim.cmd.colorscheme("aether")

			-- Enable hot reload
			require("aether.hotreload").setup()
		end,
	},
	{
		"LazyVim/LazyVim",
		opts = {
			colorscheme = "aether",
		},
	},
}
