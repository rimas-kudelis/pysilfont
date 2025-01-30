__url__ = 'https://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2024-2025, SIL Global (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'
"""
SIL fontbakery profile for version 0.13.X
"""
# pylint: disable=line-too-long  # This is data, not code
PROFILE = {
    "check_definitions": ["silfont.fbtests.checks"],
    "sections": {
        "SIL checks": [
            "silfonts/name/version_format",
            "silfonts/number_widths",
            "silfonts/repo/executable_bits",
            "silfonts/repo/FONTLOG",
            "silfonts/repo/is_OFL_FAQ_present_and_current",
            "silfonts/repo/is_OFL_URL_current",
            "silfonts/whitespace_widths",
        ],
        "Font Bakery checks": [
            "adobefonts/family/consistent_upm",
            "adobefonts/nameid_1_win_english",
            "alt_caron",
            "arabic_high_hamza",
            "arabic_spacing_symbols",
            "case_mapping",
            "control_chars",
            "dotted_circle",
            "family/single_directory",
            "family/vertical_metrics",
            "family/win_ascent_and_descent",
            "file_size",
            "googlefonts/canonical_filename",
            "googlefonts/family/equal_codepoint_coverage",
            "googlefonts/family/italics_have_roman_counterparts",
            "googlefonts/family_name_compliance",
            "googlefonts/family/tnum_horizontal_metrics",
            "googlefonts/font_names",
            "googlefonts/fstype",
            "googlefonts/name/description_max_length",
            "googlefonts/name/familyname_first_char",
            "googlefonts/name/mandatory_entries",
            "googlefonts/use_typo_metrics",
            "googlefonts/unitsperem",
            "gpos7",
            "hinting_impact",
            "integer_ppem_if_hinted",
            "linegaps",
            "mandatory_glyphs",
            "missing_small_caps_glyphs",
            "name/family_and_style_max_length",
            "name/no_copyright_on_description",
            "nested_components",
            "notofonts/cmap/unexpected_subtables",
            "notofonts/unicode_range_bits",
            "opentype/caret_slope",
            "opentype/cff_ascii_strings",
            "opentype/code_pages",
            "opentype/family/bold_italic_unique_for_nameid1",
            "opentype/family/consistent_family_name",
            "opentype/family/equal_font_versions",
            "opentype/family/max_4_fonts_per_family_name",
            "opentype/family_naming_recommendations",
            "opentype/family/panose_familytype",
            "opentype/family/underline_thickness",
            "opentype/font_version",
            "opentype/fsselection",
            "opentype/gdef_mark_chars",
            "opentype/gdef_non_mark_chars",
            "opentype/gdef_spacing_marks",
            "opentype/glyf_non_transformed_duplicate_components",
            "opentype/glyf_unused_data",
            "opentype/italic_angle",
            "opentype/kern_table",
            "opentype/layout_valid_feature_tags",
            "opentype/layout_valid_language_tags",
            "opentype/layout_valid_script_tags",
            "opentype/loca/maxp_num_glyphs",
            "opentype/mac_style",
            "opentype/maxadvancewidth",
            "opentype/monospace",
            "opentype/name/empty_records",
            "opentype/name/match_familyname_fullfont",
            "opentype/name/postscript_name_consistency",
            "opentype/postscript_name",
            "opentype/post_table_version",
            "opentype/vendor_id",
            "os2_metrics_match_hhea",
            "ots",
            "googlefonts/render_own_name",
            "required_tables",
            "sfnt_version",
            "STAT_in_statics",
            "stylisticset_description",
            "tabular_kerning",
            "transformed_components",
            "ttx_roundtrip",
            "typenetwork/weightclass",
            "unique_glyphnames",
            "unreachable_glyphs",
            "unwanted_aat_tables",
            "unwanted_tables",
            "valid_glyphnames",
            "whitespace_glyphs",
            "whitespace_ink",
            "whitespace_widths"
        ],
        "New checks from 0.12.10/Aug 2024": [
            "designspace_has_consistent_codepoints",
            "designspace_has_consistent_glyphset",
            "designspace_has_default_master",
            "designspace_has_sources",
            "empty_letters",
            "fontwerk/style_linking",
            "googlefonts/production_glyphs_similarity",
            "googlefonts/vertical_metrics_regressions",
            "name_id_1",
            "name_id_2",
            "name/italic_names",
            "name_length_req",
            "no_mac_entries",
            "opentype/xavgcharwidth",
            "rupee",
            "smallcaps_before_ligatures",
            "tnum_glyphs_equal_widths",
            "typenetwork/family/duplicated_names",
            "typenetwork/family/tnum_horizontal_metrics",
            "typenetwork/family/valid_strikeout",
            "typenetwork/family/valid_underline",
            "typenetwork/font_is_centered_vertically",
            "typenetwork/marks_width",
            "typenetwork/name/mandatory_entries",
            "typoascender_exceeds_Agrave",
            "vtt_volt_data"
        ],
        "New checks from 0.13.X/November/December 2024": [
            "caps_vertically_centered",
            "cjk_chws_feature",
            "cjk_not_enough_glyphs",
            "color_cpal_brightness",
            "googlefonts/colorfont_tables",
            "contour_count",
            "designspace_has_consistent_groups",
            "empty_glyph_on_gid1_for_colrv0",
            "fontbakery_version",
            "freetype_rasterizer",
            "fvar_name_entries",
            "googlefonts/cjk_vertical_metrics",
            "googlefonts/cjk_vertical_metrics_regressions",
            "googlefonts/description/broken_links",
            "googlefonts/description/eof_linebreak",
            "googlefonts/description/family_update",
            "googlefonts/description/git_url",
            "googlefonts/description/has_article",
            "googlefonts/description/has_unsupported_elements",
            "googlefonts/description/min_length",
            "googlefonts/description/urls",
            "googlefonts/description/valid_html",
            "googlefonts/family/has_license",
            "googlefonts/gasp",
            "googlefonts/glyphsets/shape_languages",
            "googlefonts/has_ttfautohint_params",
            "googlefonts/metadata/axisregistry_bounds",
            "googlefonts/metadata/axisregistry_valid_tags",
            "googlefonts/metadata/broken_links",
            "googlefonts/metadata/canonical_style_names",
            "googlefonts/metadata/canonical_weight_value",
            "googlefonts/metadata/can_render_samples",
            "googlefonts/metadata/category",
            "googlefonts/metadata/category_hints",
            "googlefonts/metadata/consistent_axis_enumeration",
            "googlefonts/metadata/consistent_repo_urls",
            "googlefonts/metadata/date_added",
            "googlefonts/metadata/designer_profiles",
            "googlefonts/metadata/designer_values",
            "googlefonts/metadata/empty_designer",
            "googlefonts/metadata/escaped_strings",
            "googlefonts/metadata/family_directory_name",
            "googlefonts/metadata/familyname",
            "googlefonts/metadata/filenames",
            "googlefonts/metadata/has_regular",
            "googlefonts/metadata/includes_production_subsets",
            "googlefonts/metadata/license",
            "googlefonts/metadata/match_filename_postscript",
            "googlefonts/metadata/match_fullname_postscript",
            "googlefonts/metadata/match_name_familyname",
            "googlefonts/metadata/match_weight_postscript",
            "googlefonts/metadata/menu_and_latin",
            "googlefonts/metadata/minisite_url",
            "googlefonts/metadata/nameid/family_and_full_names",
            "googlefonts/metadata/nameid/font_name",
            "googlefonts/metadata/nameid/post_script_name",
            "googlefonts/metadata/weightclass",
            "googlefonts/metadata/primary_script",
            "googlefonts/metadata/regular_is_400",
            "googlefonts/metadata/reserved_font_name",
            "googlefonts/metadata/single_cjk_subset",
            "googlefonts/metadata/subsets_order",
            "googlefonts/metadata/undeclared_fonts",
            "googlefonts/metadata/unique_full_name_values",
            "googlefonts/metadata/unique_weight_style_pairs",
            "googlefonts/metadata/unsupported_subsets",
            "googlefonts/metadata/valid_filename_values",
            "googlefonts/metadata/valid_full_name_values",
            "googlefonts/metadata/valid_nameid25",
            "googlefonts/metadata/valid_post_script_name_values",
            "googlefonts/meta/script_lang_tags",
            "googlefonts/name/version_format",
            "googlefonts/old_ttfautohint",
            "googlefonts/repo/dirname_matches_nameid_1",
            "googlefonts/repo/fb_report",
            "googlefonts/repo/sample_image",
            "googlefonts/repo/upstream_yaml_has_required_fields",
            "googlefonts/repo/vf_has_static_fonts",
            "googlefonts/weightclass",
            "googlefonts/vendor_id",
            "googlefonts/version_bump",
            "googlefonts/vertical_metrics",
            "interpolation_issues",
            "legacy_accents",
            "ligature_carets",
            "math_signs_width",
            "name/char_restrictions",
            "name/trailing_spaces",
            "opentype/cff2_call_depth",
            "opentype/cff_call_depth",
            "opentype/cff_deprecated_operators",
            "opentype/name/postscript_vs_cff",
            "opentype/points_out_of_bounds",
            "opentype/slant_direction",
            "opentype/unitsperem",
            "outline_alignment_miss",
            "outline_colinear_vectors",
            "outline_direction",
            "outline_jaggy_segments",
            "outline_semi_vertical",
            "outline_short_segments",
            "overlapping_path_segments",
            "shaping/collides",
            "shaping/forbidden",
            "shaping/regression",
            "smart_dropout",
            "soft_dotted",
            "superfamily/list",
            "superfamily/vertical_metrics",
            "ufo_consistent_curve_type",
            "ufo_features_default_languagesystem",
            "ufolint",
            "ufo_no_open_corners",
            "ufo_recommended_fields",
            "ufo_required_fields",
            "ufo_unnecessary_fields"
         ],
        "New checks from 0.13.X/January 2025": [
            "STAT_strings",
            "googlefonts/metadata/parses",
            "opentype/weight_class_fvar", 
            "cmap/format_12"
         ],
    },
    "overrides": {
        "alt_caron": [
            {
                "code": "decomposed-outline",
                "status": "PASS",
                "reason": "some SIL fonts intentionally use decomposed outlines for Lcaron, dcaron, lcaron and tcaron."
            }
            ],
        "legacy_accents": [
            {
                "code": "legacy-accent-components",
                "status": "PASS",
                "reason": "SIL disagrees with the premise of this check."
            }
        ],
        "whitespace_glyphs": [
            {
                "code": "missing-whitespace-glyph-0x00A0",
                "status": "WARN",
                "reason": "this is not as severe as assessed in the original check for 0x00A0.",
            }
        ],
    },
    "configuration_defaults": {
        "file_size": {
            "WARN_SIZE": 1 * 1024 * 1024,
            "FAIL_SIZE": 9 * 1024 * 1024,
        }
    },
}
