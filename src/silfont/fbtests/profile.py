__url__ = 'https://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2024-2025, SIL Global (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'David Raymond, Bob Hallissy, Nicolas Spalinger'
"""
SIL fontbakery profile for version 0.13.3+
"""
# pylint: disable=line-too-long  # This is data, not code
PROFILE = {
    "check_definitions": ["silfont.fbtests.checks"],
    "sections": {
        "SIL checks": [
            "silfonts/name/version_format",
            "silfonts/number_widths",
            "silfonts/repo/FONTLOG",
            "silfonts/repo/executable_bits",
            "silfonts/repo/is_OFL_FAQ_present_and_current",
            "silfonts/repo/is_OFL_URL_current",
            "silfonts/repo/new_preferred_dba_sil_global",
            "silfonts/whitespace_widths"
        ],
        "Font Bakery checks": [
            "adobefonts/family/consistent_upm",
            "adobefonts/nameid_1_win_english",
            "alt_caron",
            "arabic_high_hamza",
            "arabic_spacing_symbols",
            "base_has_width",
            "case_mapping",
            "contour_count", 
            "control_chars",
            "designspace_has_consistent_codepoints",
            "designspace_has_consistent_glyphset",
            "designspace_has_consistent_groups",
            "designspace_has_default_master",
            "designspace_has_sources",
            "dotted_circle",
            "empty_letters",
            "family/single_directory",
            "family/vertical_metrics",
            "file_size",
            "fontwerk/style_linking",
            "freetype_rasterizer",
            "googlefonts/canonical_filename",
            "googlefonts/family/equal_codepoint_coverage",
            "googlefonts/family/italics_have_roman_counterparts",
            "googlefonts/family_name_compliance",
            "googlefonts/family/tnum_horizontal_metrics",
            "googlefonts/font_names",
            "googlefonts/fstype",
            "googlefonts/gasp",
            "googlefonts/glyphsets/shape_languages",
            "googlefonts/name/description_max_length",
            "googlefonts/name/familyname_first_char",
            "googlefonts/name/mandatory_entries",
            "googlefonts/production_glyphs_similarity",
            "googlefonts/render_own_name",
            "googlefonts/use_typo_metrics",
            "googlefonts/vendor_id",
            "googlefonts/vertical_metrics",
            "googlefonts/vertical_metrics_regressions",
            "googlefonts/weightclass",
            "gpos7",
            "gpos_kerning_info",
            "hinting_impact",
            "integer_ppem_if_hinted",
            "legacy_accents",
            "linegaps",
            "mandatory_glyphs",
            "microsoft/copyright",
            "microsoft/vertical_metrics",
            "missing_small_caps_glyphs",
            "name/char_restrictions",
            "name/family_and_style_max_length",
            "name_id_1",
            "name_id_2",
            "name/italic_names",
            "name_length_req",
            "name/no_copyright_on_description",
            "name/trailing_spaces",
            "nested_components",
            "no_mac_entries",
            "notofonts/cmap/unexpected_subtables",
            "notofonts/unicode_range_bits",
            "opentype/caret_slope",
            "opentype/code_pages",
            "opentype/dsig",
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
            "opentype/points_out_of_bounds",
            "opentype/postscript_name",
            "opentype/post_table_version",
            "opentype/unitsperem",
            "opentype/unwanted_aat_tables",
            "opentype/varfont/family_axis_ranges",
            "opentype/vendor_id",
            "opentype/xavgcharwidth",
            "os2_metrics_match_hhea",
            "ots",
            "outline_alignment_miss",
            "outline_colinear_vectors",
            "outline_direction",
            "outline_jaggy_segments",
            "outline_semi_vertical",
            "outline_short_segments",
            "overlapping_path_segments",
            "required_tables",
            "rupee",
            "sfnt_version",
            "smallcaps_before_ligatures",
            "smart_dropout",
            "stylisticset_description",
            "tabular_kerning",
            "tnum_glyphs_equal_widths",
            "transformed_components",
            "ttx_roundtrip",
            "typenetwork/family/duplicated_names",
            "typenetwork/family/equal_numbers_of_glyphs",
            "typenetwork/family/tnum_horizontal_metrics",
            "typenetwork/family/valid_strikeout",
            "typenetwork/family/valid_underline",
            "typenetwork/name/mandatory_entries",
            "typenetwork/vertical_metrics",
            "typenetwork/weightclass",
            "typoascender_exceeds_Agrave",
            "ufo_consistent_curve_type",
            "ufo_features_default_languagesystem",
            "ufolint",
            "ufo_no_open_corners",
            "ufo_recommended_fields",
            "ufo_required_fields",
            "ufo_unnecessary_fields",
            "unique_glyphnames",
            "unreachable_glyphs",
            "unwanted_tables",
            "valid_glyphnames",
            "vtt_volt_data",
            "whitespace_glyphs",
            "whitespace_ink",
            "whitespace_widths"
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
        "opentype/family_naming_recommendations": [
            {
                # bh: This override is experimental to see if it is too noisy:
                # Change messages about name strings being too long from INFO to WARN
                # so they show up in our fontbakery reports.
                "code": "bad-entries",
                "status": "WARN",
                "reason": "change from INFO to WARN so it shows up in our build results."
            }
        ],
        "whitespace_glyphs": [
            {
                "code": "missing-whitespace-glyph-0x00A0",
                "status": "WARN",
                "reason": "this is not as severe as assessed in the original check for 0x00A0.",
            }
        ],
        "contour_count": [
            {
                "code": "contour-count",
                "status" : "INFO",
                "reason" : "SIL trusts designers, is concerned only with 'no-contour' results",
            }
        ],
        "unwanted_tables": [
            {
                "code": "unwanted-tables",
                "status" : "WARN",
                "reason" : "It's fine to have a fontTools Debg table in your font when developing since it's very useful for debugging, just make sure it gets removed when making a release",
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
