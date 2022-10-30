AUTHOR = 'Sebastien Chiasson'
SITENAME = 'sjchiass'
#SITEURL = 'https://sjchiass.com'
SITENAME = "Errata"
SITETITLE = "Errata Blog"
SITESUBTITLE = "Cats, hobbies, etc"
SITEDESCRIPTION = "A blog mostly about electronics, cats and some coding"
SITELOGO = "/images/logo.png"
FAVICON = "/images/logo.png"

PATH = 'content'
THEME = "./Flex"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True

TIMEZONE = 'Canada/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Main Menu
MAIN_MENU = True
MENUITEMS = (("Archives", "/archives"), ("Categories", "/categories"), ("Tags", "/tags"),)

# Blogroll
LINKS = (("Live plant feed", "https://plants.sjchiass.com/"),)

# Social widget
SOCIAL = (("github", "https://www.github.com/sjchiass"),
            ("youtube", "https://www.youtube.com/@sjchiass"),
            ("twitter", "https://twitter.com/sjchiass"),
            ("instagram", "https://www.instagram.com/sjchiass/"),
            ("facebook", "https://www.facebook.com/sjchiass"),)

PLUGINS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
