{
  'variables': {
    'depth': '..',
    'feature_defines': [
      'ENABLE_DATABASE=1',
      'ENABLE_DASHBOARD_SUPPORT=0',
      'ENABLE_JAVASCRIPT_DEBUGGER=0',
      'ENABLE_JSC_MULTIPLE_THREADS=0',
      'ENABLE_ICONDATABASE=0',
      'ENABLE_XSLT=1',
      'ENABLE_XPATH=1',
      'ENABLE_SVG=1',
      'ENABLE_SVG_ANIMATION=1',
      'ENABLE_SVG_AS_IMAGE=1',
      'ENABLE_SVG_USE=1',
      'ENABLE_SVG_FOREIGN_OBJECT=1',
      'ENABLE_SVG_FONTS=1',
      'ENABLE_VIDEO=1',
      'ENABLE_WORKERS=0',
    ],
  },
  'includes': [
    '../build/common.gypi',
    '../build/external_code.gypi',
  ],
  'target_defaults': {
    'include_dirs': [
      '..',
    ],
    'defines': [
      '<@(feature_defines)',
      'BUILDING_CHROMIUM__=1',
      'USE_GOOGLE_URL_LIBRARY=1',
      'USE_SYSTEM_MALLOC=1',
    ],
    'conditions': [
      ['OS=="mac"', {
        'defines': [
          ['WEBCORE_NAVIGATOR_PLATFORM_', '"FixMeAndRemoveTrailingUnderscore"'],
        ],
      }],
      ['OS=="win"', {
        'defines': [
          ['CRASH', '__debugbreak'],
          ['WEBCORE_NAVIGATOR_PLATFORM', '"Win32"'],
        ],
      }],
    ],
    'sources/': [
      ['exclude', '(Mac|Win|Pthreads)\\.(cpp|mm)$'],
    ],
    'conditions': [
      ['OS=="mac"', {'sources/': [['include', '(Mac|Pthreads)\\.(cpp|mm)$']]}],
      ['OS=="win"', {'sources/': [['include', 'Win\\.cpp$']]}],
    ],
  },
  'targets': [
    {
      'target_name': 'wtf',
      'type': 'static_library',
      'include_dirs': [
        '../third_party/WebKit/JavaScriptCore',
        '../third_party/WebKit/JavaScriptCore/wtf',
        '../third_party/WebKit/JavaScriptCore/wtf/unicode',
      ],
      'sources': [
        '../third_party/WebKit/JavaScriptCore/wtf/chromium/ChromiumThreading.h',
        '../third_party/WebKit/JavaScriptCore/wtf/chromium/MainThreadChromium.cpp',
        #'../third_party/WebKit/JavaScriptCore/wtf/gtk/MainThreadGtk.cpp',
        #'../third_party/WebKit/JavaScriptCore/wtf/mac/MainThreadMac.mm',
        #'../third_party/WebKit/JavaScriptCore/wtf/qt/MainThreadQt.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/unicode/icu/CollatorICU.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/unicode/icu/UnicodeIcu.h',
        #'../third_party/WebKit/JavaScriptCore/wtf/unicode/qt4/UnicodeQt4.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/unicode/Collator.h',
        #'../third_party/WebKit/JavaScriptCore/wtf/unicode/CollatorDefault.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/unicode/Unicode.h',
        '../third_party/WebKit/JavaScriptCore/wtf/unicode/UTF8.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/unicode/UTF8.h',
        #'../third_party/WebKit/JavaScriptCore/wtf/win/MainThreadWin.cpp',
        #'../third_party/WebKit/JavaScriptCore/wtf/wx/MainThreadWx.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/AlwaysInline.h',
        '../third_party/WebKit/JavaScriptCore/wtf/ASCIICType.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Assertions.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/Assertions.h',
        '../third_party/WebKit/JavaScriptCore/wtf/AVLTree.h',
        '../third_party/WebKit/JavaScriptCore/wtf/ByteArray.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/ByteArray.h',
        '../third_party/WebKit/JavaScriptCore/wtf/CurrentTime.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/CurrentTime.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Deque.h',
        '../third_party/WebKit/JavaScriptCore/wtf/FastMalloc.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/FastMalloc.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Forward.h',
        #'../third_party/WebKit/JavaScriptCore/wtf/GOwnPtr.cpp',
        #'../third_party/WebKit/JavaScriptCore/wtf/GOwnPtr.h',
        '../third_party/WebKit/JavaScriptCore/wtf/GetPtr.h',
        '../third_party/WebKit/JavaScriptCore/wtf/HashCountedSet.h',
        '../third_party/WebKit/JavaScriptCore/wtf/HashFunctions.h',
        '../third_party/WebKit/JavaScriptCore/wtf/HashIterators.h',
        '../third_party/WebKit/JavaScriptCore/wtf/HashMap.h',
        '../third_party/WebKit/JavaScriptCore/wtf/HashSet.h',
        '../third_party/WebKit/JavaScriptCore/wtf/HashTable.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/HashTable.h',
        '../third_party/WebKit/JavaScriptCore/wtf/HashTraits.h',
        '../third_party/WebKit/JavaScriptCore/wtf/ListHashSet.h',
        '../third_party/WebKit/JavaScriptCore/wtf/ListRefPtr.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Locker.h',
        '../third_party/WebKit/JavaScriptCore/wtf/MainThread.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/MainThread.h',
        '../third_party/WebKit/JavaScriptCore/wtf/MallocZoneSupport.h',
        '../third_party/WebKit/JavaScriptCore/wtf/MathExtras.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Noncopyable.h',
        '../third_party/WebKit/JavaScriptCore/wtf/NotFound.h',
        '../third_party/WebKit/JavaScriptCore/wtf/OwnArrayPtr.h',
        '../third_party/WebKit/JavaScriptCore/wtf/OwnPtr.h',
        #'../third_party/WebKit/JavaScriptCore/wtf/OwnPtrWin.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/PassRefPtr.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Platform.h',
        '../third_party/WebKit/JavaScriptCore/wtf/PtrAndFlags.h',
        '../third_party/WebKit/JavaScriptCore/wtf/RandomNumber.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/RandomNumber.h',
        '../third_party/WebKit/JavaScriptCore/wtf/RandomNumberSeed.h',
        '../third_party/WebKit/JavaScriptCore/wtf/RefCounted.h',
        '../third_party/WebKit/JavaScriptCore/wtf/RefCountedLeakCounter.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/RefCountedLeakCounter.h',
        '../third_party/WebKit/JavaScriptCore/wtf/RefPtr.h',
        '../third_party/WebKit/JavaScriptCore/wtf/RefPtrHashMap.h',
        '../third_party/WebKit/JavaScriptCore/wtf/RetainPtr.h',
        '../third_party/WebKit/JavaScriptCore/wtf/StdLibExtras.h',
        '../third_party/WebKit/JavaScriptCore/wtf/StringExtras.h',
        '../third_party/WebKit/JavaScriptCore/wtf/TCPackedCache.h',
        '../third_party/WebKit/JavaScriptCore/wtf/TCPageMap.h',
        '../third_party/WebKit/JavaScriptCore/wtf/TCSpinLock.h',
        '../third_party/WebKit/JavaScriptCore/wtf/TCSystemAlloc.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/TCSystemAlloc.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Threading.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/Threading.h',
        #'../third_party/WebKit/JavaScriptCore/wtf/ThreadingGtk.cpp',
        #'../third_party/WebKit/JavaScriptCore/wtf/ThreadingNone.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/ThreadingPthreads.cpp',
        #'../third_party/WebKit/JavaScriptCore/wtf/ThreadingQt.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/ThreadingWin.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/ThreadSpecific.h',
        '../third_party/WebKit/JavaScriptCore/wtf/ThreadSpecificWin.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/TypeTraits.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/TypeTraits.h',
        '../third_party/WebKit/JavaScriptCore/wtf/UnusedParam.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Vector.h',
        '../third_party/WebKit/JavaScriptCore/wtf/VectorTraits.h',
        '../third_party/WebKit/JavaScriptCore/wtf/dtoa.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/dtoa.h',
        'build/precompiled_webkit.cc',
        'build/precompiled_webkit.h',
      ],
      'sources!': [
        'build/precompiled_webkit.cc',
        'build/precompiled_webkit.h',
      ],
      'dependencies': [
        '../third_party/icu38/icu38.gyp:icui18n',
        '../third_party/icu38/icu38.gyp:icuuc',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../third_party/WebKit/JavaScriptCore',
        ],
      },
      'export_dependent_settings': [
        '../third_party/icu38/icu38.gyp:icui18n',
        '../third_party/icu38/icu38.gyp:icuuc',
      ],
      'conditions': [
        ['OS=="win"', {
          'defines': [
            '__STD_C',
            '_SCL_SECURE_NO_DEPRECATE',
            '_CRT_SECURE_NO_DEPRECATE',
          ],
          'include_dirs': [
            'build/JavaScriptCore',
            '../third_party/WebKit/JavaScriptCore/os-win32',
          ],
          'configurations': {
            'Debug': {
              'msvs_precompiled_header': 'build/precompiled_webkit.h',
              'msvs_precompiled_source': 'build/precompiled_webkit.cc',
            },
          },
        }],
      ],
      'msvs_disabled_warnings': [4127, 4355, 4510, 4512, 4610, 4706],
    },
    {
      'target_name': 'v8config',
      'type': 'none',
      'actions': [
        {
          'action_name': 'config.h',
          'inputs': [
            'config.h.in',
            '../third_party/WebKit/WebCore/bridge/npapi.h',
            '../third_party/WebKit/WebCore/bridge/npruntime.h',
            'port/bindings/v8/npruntime_priv.h',
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/v8/config.h',
            '<(INTERMEDIATE_DIR)/v8/javascript/npapi.h',
            '<(INTERMEDIATE_DIR)/v8/javascript/npruntime.h',
            '<(INTERMEDIATE_DIR)/v8/javascript/npruntime_priv.h',
          ],
          'conditions': [
            ['OS=="win"', {
              'inputs': ['../third_party/WebKit/JavaScriptCore/os-win32/stdint.h'],
              'outputs': ['<(INTERMEDIATE_DIR)/v8/javascript/stdint.h'],
            }],
          ],
          'action': 'python action_jsconfig.py v8 <(INTERMEDIATE_DIR)/v8 <(_inputs)',
        },
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(INTERMEDIATE_DIR)/v8',
        ],
      },
    },
    {
      'target_name': 'v8bindings',
      'type': 'static_library',
      'dependencies': [
        'wtf',
        'v8config',
      ],
      'rules': [
        # Some of these rules don't seem to belong in jsbindings.
        {
          'rule_name': 'bison',
          'extension': 'y',
          'outputs': [
            '<(INTERMEDIATE_DIR)/*.cpp',
            '<(INTERMEDIATE_DIR)/*.h'
          ],
          'action': 'python rule_bison.py * <(INTERMEDIATE_DIR)',
          'process_outputs_as_sources': 1,
        },
        {
          'rule_name': 'gperf',
          'extension': 'gperf',
          # gperf output is only ever #included by other source files.  As
          # such, process_outputs_as_sources is off.  Some gperf output is
          # #included as *.c and some as *.cpp.  Since there's no way to tell
          # which one will be needed in a rule definition, declare both as
          # outputs.  The harness script will generate one file and copy it to
          # the other.
          'outputs': [
            '<(INTERMEDIATE_DIR)/*.c',
            '<(INTERMEDIATE_DIR)/*.cpp',
          ],
          'action': 'python rule_gperf.py * <(INTERMEDIATE_DIR)',
          'process_outputs_as_sources': 0,
        },
      ],
      'sources': [
        # bison rule
        '../third_party/WebKit/WebCore/css/CSSGrammar.y',
        '../third_party/WebKit/WebCore/xml/XPathGrammar.y',
        # gperf rule
        '../third_party/WebKit/WebCore/html/DocTypeStrings.gperf',
        '../third_party/WebKit/WebCore/html/HTMLEntityNames.gperf',
        '../third_party/WebKit/WebCore/platform/ColorData.gperf',
      ],
      'include_dirs': [
        '<(INTERMEDIATE_DIR)',
        '../third_party/WebKit/WebCore/css',
        '../third_party/WebKit/WebCore/dom',
        '../third_party/WebKit/WebCore/html',
        '../third_party/WebKit/WebCore/loader',
        '../third_party/WebKit/WebCore/page',
        '../third_party/WebKit/WebCore/platform',
        '../third_party/WebKit/WebCore/platform/graphics',
        '../third_party/WebKit/WebCore/platform/graphics/transforms',
        '../third_party/WebKit/WebCore/platform/network',
        '../third_party/WebKit/WebCore/platform/network/chromium',
        '../third_party/WebKit/WebCore/platform/text',
        '../third_party/WebKit/WebCore/svg',
        '../third_party/WebKit/WebCore/svg/animation',
        '../third_party/WebKit/WebCore/svg/graphics',
        '../third_party/WebKit/WebCore/xml',
      ],
      'xcode_framework_dirs': [
        '$(SDKROOT)/System/Library/Frameworks/ApplicationServices.framework/Frameworks',
      ],
      'actions': [
        # Many of these actions don't seem to belong in jsbindings, but
        # jsbindings depends on them and doesn't have any other dependencies
        # that require them.
        {
          'action_name': 'CSSPropertyNames',
          'inputs': [
            '../third_party/WebKit/WebCore/css/makeprop.pl',
            '../third_party/WebKit/WebCore/css/CSSPropertyNames.in',
            '../third_party/WebKit/WebCore/css/SVGCSSPropertyNames.in',
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/CSSPropertyNames.cpp',
            '<(INTERMEDIATE_DIR)/CSSPropertyNames.gperf',
            '<(INTERMEDIATE_DIR)/CSSPropertyNames.h',
            '<(INTERMEDIATE_DIR)/CSSPropertyNames.in',
          ],
          'action': 'python action_csspropertynames.py <(_inputs) <(_outputs)',
        },
        {
          'action_name': 'CSSValueKeywords',
          'inputs': [
            '../third_party/WebKit/WebCore/css/makevalues.pl',
            '../third_party/WebKit/WebCore/css/CSSValueKeywords.in',
            '../third_party/WebKit/WebCore/css/SVGCSSValueKeywords.in',
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/CSSValueKeywords.c',
            '<(INTERMEDIATE_DIR)/CSSValueKeywords.gperf',
            '<(INTERMEDIATE_DIR)/CSSValueKeywords.h',
            '<(INTERMEDIATE_DIR)/CSSValueKeywords.in',
          ],
          'action': 'python action_cssvaluekeywords.py <(_inputs) <(_outputs)',
        },
        {
          'action_name': 'HTMLNames',
          'inputs': [
            '../third_party/WebKit/WebCore/dom/make_names.pl',
            '../third_party/WebKit/WebCore/html/HTMLTagNames.in',
            '../third_party/WebKit/WebCore/html/HTMLAttributeNames.in',
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/HTMLNames.cpp',
            '<(INTERMEDIATE_DIR)/HTMLNames.h',
            # Pass --wrapperFactory to make_names to get these (JSC build?)
            #'<(INTERMEDIATE_DIR)/JSHTMLElementWrapperFactory.cpp',
            #'<(INTERMEDIATE_DIR)/JSHTMLElementWrapperFactory.h',
          ],
          'action': 'python action_makenames.py <(_outputs) -- <(_inputs) -- --extraDefines "<(feature_defines)"',
          'process_outputs_as_sources': 1,
        },
        {
          'action_name': 'SVGNames',
          'inputs': [
            '../third_party/WebKit/WebCore/dom/make_names.pl',
            '../third_party/WebKit/WebCore/svg/svgtags.in',
            '../third_party/WebKit/WebCore/svg/svgattrs.in',
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/SVGNames.cpp',
            '<(INTERMEDIATE_DIR)/SVGNames.h',
            '<(INTERMEDIATE_DIR)/SVGElementFactory.cpp',
            '<(INTERMEDIATE_DIR)/SVGElementFactory.h',
            # Pass --wrapperFactory to make_names to get these (JSC build?)
            #'<(INTERMEDIATE_DIR)/JSSVGElementWrapperFactory.cpp',
            #'<(INTERMEDIATE_DIR)/JSSVGElementWrapperFactory.h',
          ],
          'action': 'python action_makenames.py <(_outputs) -- <(_inputs) -- --factory --extraDefines "<(feature_defines)"',
          'process_outputs_as_sources': 1,
        },
        {
          'action_name': 'UserAgentStyleSheets',
          'inputs': [
            '../third_party/WebKit/WebCore/css/make-css-file-arrays.pl',
            '../third_party/WebKit/WebCore/css/html4.css',
            '../third_party/WebKit/WebCore/css/quirks.css',
            '../third_party/WebKit/WebCore/css/view-source.css',
            '../third_party/WebKit/WebCore/css/themeWin.css',
            '../third_party/WebKit/WebCore/css/themeWinQuirks.css',
            '../third_party/WebKit/WebCore/css/svg.css',
            '../third_party/WebKit/WebCore/css/mediaControls.css',
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/UserAgentStyleSheets.h',
            '<(INTERMEDIATE_DIR)/UserAgentStyleSheetsData.cpp',
          ],
          'action': 'python action_useragentstylesheets.py <(_outputs) -- <(_inputs)',
          'process_outputs_as_sources': 1,
        },
        {
          'action_name': 'XLinkNames',
          'inputs': [
            '../third_party/WebKit/WebCore/dom/make_names.pl',
            '../third_party/WebKit/WebCore/svg/xlinkattrs.in',
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/XLinkNames.cpp',
            '<(INTERMEDIATE_DIR)/XLinkNames.h',
          ],
          'action': 'python action_makenames.py <(_outputs) -- <(_inputs) -- --extraDefines "<(feature_defines)"',
          'process_outputs_as_sources': 1,
        },
        {
          'action_name': 'XMLNames',
          'inputs': [
            '../third_party/WebKit/WebCore/dom/make_names.pl',
            '../third_party/WebKit/WebCore/xml/xmlattrs.in',
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/XMLNames.cpp',
            '<(INTERMEDIATE_DIR)/XMLNames.h',
          ],
          'action': 'python action_makenames.py <(_outputs) -- <(_inputs) -- --extraDefines "<(feature_defines)"',
          'process_outputs_as_sources': 1,
        },
        {
          'action_name': 'tokenizer',
          'inputs': [
            '../third_party/WebKit/WebCore/css/maketokenizer',
            '../third_party/WebKit/WebCore/css/tokenizer.flex',
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/tokenizer.cpp',
          ],
          'action': 'python action_maketokenizer.py <(_outputs) -- <(_inputs)',
        },
      ],
    },
  ],
  'conditions': [
    ['OS=="win"', {
      'targets': [
        {
          'target_name': 'webkit_resources',
          'type': 'none',
          'sources': [
            'glue/webkit_resources.grd',
          ],
          'msvs_tool_files': ['../tools/grit/build/grit_resources.rules'],
          'direct_dependent_settings': {
            'include_dirs': [
              '$(OutDir)/grit_derived_sources',
            ],
          },
        },
      ],
    }],
  ],
}
