{
  "targets": [
    {
      "target_name": "IconExtractor",
      "includes": [
        "auto.gypi"
      ],
      "include_dirs": [
        "<!(node -p \"require('node-addon-api').include_dir\")"
      ],
      "dependencies": [
        "<!(node -p \"require('node-addon-api').gyp\")"
      ], 
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      },
      "conditions": [
        ['OS=="win"', {
          'sources': [
      "src/IconExtractor.cpp"
	    "src/IconExtractorWindows.cpp"
          ],
          "libraries": [
            "-lGdiplus"
          ],
        }],
      ]
    }
  ]
}
