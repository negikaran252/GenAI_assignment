# dictionary for converting language to code for translating    
language_code_dict = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Assamese": "as",
    "Azerbaijani (Latin)": "az",
    "Bangla": "bn",
    "Bashkir": "ba",
    "Basque": "eu",
    "Bosnian (Latin)": "bs",
    "Bulgarian": "bg",
    "Cantonese (Traditional)": "yue",
    "Catalan": "ca",
    "Chinese (Literary)": "lzh",
    "Chinese Simplified": "zh-Hans",
    "Chinese Traditional": "zh-Hant",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dari": "prs",
    "Divehi": "dv",
    "Dutch": "nl",
    "English": "en",
    "Estonian": "et",
    "Faroese": "fo",
    "Fijian": "fj",
    "Filipino": "fil",
    "Finnish": "fi",
    "French": "fr",
    "French (Canada)": "fr-ca",
    "Galician": "gl",
    "Georgian": "ka",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Haitian Creole": "ht",
    "Hebrew": "he",
    "Hindi": "hi",
    "Hmong Daw (Latin)": "mww",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Indonesian": "id",
    "Interlingua": "ia",
    "Inuinnaqtun": "ikt",
    "Inuktitut": "iu",
    "Inuktitut (Latin)": "iu-Latn",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Kannada": "kn",
    "Kazakh (Cyrillic)": "kk, kk-cyrl",
    "Kazakh (Latin)": "kk-latn",
    "Khmer": "km",
    "Klingon": "tlh-Latn",
    "Klingon (plqaD)": "tlh-Piqd",
    "Korean": "ko",
    "Kurdish (Arabic) (Central)": "ku-arab,ku",
    "Kurdish (Latin) (Northern)": "ku-latn, kmr",
    "Kyrgyz (Cyrillic)": "ky",
    "Lao": "lo",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Macedonian": "mk",
    "Malagasy": "mg",
    "Malay (Latin)": "ms",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Maori": "mi",
    "Marathi": "mr",
    "Mongolian (Cyrillic)": "mn-Cyrl",
    "Mongolian (Traditional)": "mn-Mong",
    "Myanmar (Burmese)": "my",
    "Nepali": "ne",
    "Norwegian": "nb",
    "Odia": "or",
    "Pashto": "ps",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese (Brazil)": "pt, pt-br",
    "Portuguese (Portugal)": "pt-pt",
    "Punjabi": "pa",
    "Queretaro Otomi": "otq",
    "Romanian": "ro",
    "Russian": "ru",
    "Samoan (Latin)": "sm",
    "Serbian (Cyrillic)": "sr-Cyrl",
    "Serbian (Latin)": "sr, sr-latn",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Spanish": "es",
    "Swahili (Latin)": "sw",
    "Swedish": "sv",
    "Tahitian": "ty",
    "Tamil": "ta",
    "Tatar (Latin)": "tt",
    "Telugu": "te",
    "Thai": "th",
    "Tibetan": "bo",
    "Tigrinya": "ti",
    "Tongan": "to",
    "Turkish": "tr",
    "Turkmen (Latin)": "tk",
    "Ukrainian": "uk",
    "Upper Sorbian": "hsb",
    "Urdu": "ur",
    "Uyghur (Arabic)": "ug",
    "Uzbek (Latin)": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Yucatec Maya": "yua",
    "Zulu": "zu"
}

# dictionary for converting language to code for speech 
voice_data_dict = {
    "Afrikaans": "af-ZA",
    "Amharic": "am-ET",
    "Arabic": "ar-AE",
    "Azerbaijani": "az-AZ",
    "Bulgarian": "bg-BG",
    "Bangla": "bn-BD",
    "Bengali": "bn-IN",
    "Bosnian": "bs-BA",
    "Catalan": "ca-ES",
    "Czech": "cs-CZ",
    "Welsh": "cy-GB",
    "Danish": "da-DK",
    "German": "de-AT",
    "Greek": "el-GR",
    "English": "en-AU",
    "Spanish": "es-AR",
    "Estonian": "et-EE",
    "Basque": "eu-ES",
    "Persian": "fa-IR",
    "Finnish": "fi-FI",
    "Filipino": "fil-PH",
    "French": "fr-BE",
    "Irish": "ga-IE",
    "Galician": "gl-ES",
    "Gujarati": "gu-IN",
    "Hebrew": "he-IL",
    "Hindi": "hi-IN",
    "Croatian": "hr-HR",
    "Hungarian": "hu-HU",
    "Armenian": "hy-AM",
    "Indonesian": "id-ID",
    "Icelandic": "is-IS",
    "Italian": "it-IT",
    "Japanese": "ja-JP",
    "Javanese": "jv-ID",
    "Georgian": "ka-GE",
    "Kazakh": "kk-KZ",
    "Khmer": "km-KH",
    "Kannada": "kn-IN",
    "Korean": "ko-KR",
    "Lao": "lo-LA",
    "Lithuanian": "lt-LT",
    "Latvian": "lv-LV",
    "Macedonian": "mk-MK",
    "Malayalam": "ml-IN",
    "Mongolian": "mn-MN",
    "Marathi": "mr-IN",
    "Malay": "ms-MY",
    "Maltese": "mt-MT",
    "Burmese": "my-MM",
    "Norwegian Bokmål": "nb-NO",
    "Nepali": "ne-NP",
    "Dutch": "nl-BE",
    "Polish": "pl-PL",
    "Pashto": "ps-AF",
    "Portuguese": "pt-BR",
    "Romanian": "ro-RO",
    "Russian": "ru-RU",
    "Sinhala": "si-LK",
    "Slovak": "sk-SK",
    "Slovenian": "sl-SI",
    "Albanian": "sq-AL",
    "Serbian": "sr-BA-Cyrl",
    "Swedish": "sv-SE",
    "Swahili": "sw-KE",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Thai": "th-TH",
    "Turkish": "tr-TR",
    "Ukrainian": "uk-UA",
    "Urdu": "ur-PK",
    "Uzbek": "uz-UZ-Latn",
    "Vietnamese": "vi-VN",
    "Xhosa": "xh-ZA",
    "Yiddish": "yi-001",
    "Yoruba": "yo-NG",
    "Chinese": "zh-CN",
    "Zulu": "zu-ZA",
}
