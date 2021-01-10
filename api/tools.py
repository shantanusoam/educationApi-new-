
from api.api import Graphic_deginer
from flask import Blueprint
from flask import Flask, request, jsonify

tools = Blueprint("tools", __name__)
programming = [
            
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/4tfKlG1Ylr94FeVUQH5Oic/2bfef3e8d5536a47e52e6e5f50c258c8/og-square.png?w=640&h=640&q=50&fm=webp',
        'intro': "An interactive map of popular screen sizes showing the responsive and adaptive device landscape",
        'name': 'Screen Size Map',
        'url': 'https://www.screensizemap.com/',
    }
    ,
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5FX7FgtToDupaRBZuRFW3m/3e822bfe48221fe462ba9205ead4be9b/image.png?w=636&h=300&q=50&fm=webp',
        'intro': "Automatically remove an image background with no clicks and for free in 5 seconds.",
        'name': 'Image Background Remover',
        'url': 'https://www.remove.bg/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/3D1UOB3RrnRLcTtMytmyJa/284a58d52a99d52ded174c17790daeb8/image.png?w=800&h=421&q=50&fm=webp',
        'intro': "Create and share beautiful images of your source code.",
        'name': 'Codeimg.io',
        'url': 'https://codeimg.io/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/2SSyh2voG8mIcUlkpNDDbp/850fa97bd0d109fb16e318edbbfaa7db/image.png?w=636&h=300&q=50&fm=webp',
        'intro': "Free online tools for bulk image processing (resize, crop, compress and more).",
        'name': 'Bulk Image Processing',
        'url': 'https://www.imgbot.ai/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/71B5MfU2Oe5l9BNITmQYYi/ca1fd6bf70dbbf19879648232f4f2497/screenshot.png?w=800&h=450&q=50&fm=webp',
        'intro': "Develop responsive web apps 5x faster. A must-have DevTool for all Front-End developers that will ma",
        'name': 'Responsively',
        'url': 'https://responsively.app/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5UJgTMBsuDqpV1JVgOryvn/59e8e7289d63ba2cd2c6eb884f18014b/image.png?w=304&h=166&q=50&fm=webp',
        'intro': "The most complete resource for the best monospace coding fonts.",
        'name': 'Programming Fonts',
        'url': 'https://app.programmingfonts.org/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/11n7eqjDE3UFlt5v6OkRBT/dd0beaf8e09dc2a61c651833f3ed553f/image.png?w=800&h=416&q=50&fm=webp',
        'intro': "A tool to debug and generate meta tag code for any website.",
        'name': 'Meta Tags',
        'url': 'https://metatags.io/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/4kVxycBS3keteNdBmEDsC8/abbd160757896407cd696c964719dfda/image.png?w=175&h=175&q=50&fm=webp',
        'intro': "Lorem Ipsum... but for photos.",
        'name': 'Lorem Picsum',
        'url': 'https://picsum.photos/',
    },
     {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5iPXVJ2jpDKGyPyfcHhMJ9/36b7d3f8af92ab6703f94b6152e5c547/image.png?w=676&h=676&q=50&fm=webp',
        'intro': "Collection of open APIs (movies, weather, food, news, and more) for development",
        'name': 'Public APIs',
        'url': 'https://public-apis.xyz/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5b7A0ciaL5LU4wmb2ZYG0v/bb681d4a2c55c2b3c5aedb3479dda7e7/5aecb012-4bda-467c-9782-1ef157aec0d2?w=800&h=450&q=50&fm=webp',
        'intro': "Instantly resize and crop your photos & images for all web and social media formats with one click",
        'name': 'Free Image and Photo Resizer',
        'url': 'https://promo.com/tools/image-resizer/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/1YefYhckdPwmjhjvfUhsI7/c3371fb888864ad70bb0af1b40bf54de/image.png?w=636&h=300&q=50&fm=webp',
        'intro': "Use generative art for your image placeholders.",
        'name': 'Generative Placeholders',
        'url': 'https://generative-placeholders.glitch.me/',
    },
]





webDevelopment = [
    {
                        'name': "http://anicollection.github.io/#/",
                        'url': "collection of copy-paste animations"
                    },
                    {
                        'name': "https://daneden.github.io/animate.css/",
                        'url': "Just-add-water CSS animations"
                    },
                    {
                        'name': "http://animista.net/",
                        'url': "CSS animations on demand."
                    },
                    {
                        'name': "http://animejs.com/",
                        'url': "JavaScript animation engine."
                    },
                    {
                        'name': "https://epic-spinners.epicmax.co/#/",
                        'url': "Css only. Easy to use. VueJS integration."
                    },
                    {
                        'name': "http://tobiasahlin.com/spinkit/",
                        'url': "loading spinners animated with CSS."
                    },

                    'online code editor' [
                        {
                        'name': 'Codepen',
                        'url': 'https://codepen.io/',
                        'intro':'A development environment for front-end designers and developers, to showcase user-created HTML, CSS and JavaScript code snippets',
                    },
                    {
                        'name': 'Glitch',
                        'url': 'https://glitch.com/',
                        'intro':'An online editor where you can mix and collaborate on code',
                    },
                    {
                        'name': 'Glot.io',
                        'url': 'https://glot.io/',
                        'intro':'An open-source paste-bin with runnable snippets and API.',
                    }
                    ,
                    {
                        'name': 'Repl.it',
                        'url': 'https://repl.it/',
                        'intro':'An instant IDE to learn, build, collaborate, and host all in one place',
                    }
                    ]
                    ,
                    'Chrome extentions' [
                        {
                            'name': 'Built With Technology Analyzer',
                        'url': 'https://chrome.google.com/webstore/detail/builtwith-technology-prof/dapjbgnjinbpoindlpdmhochffioedbn?hl=en-US',
                        'intro':'Lets you see what tools and JavaScript libraries a site is using.',
                        },
                        {
                            'name': 'ColorZilla',
                        'url': 'https://chrome.google.com/webstore/detail/colorzilla/bhlhnicpbhignbdhedgjhgdocnmhomnp',
                        'intro':'Find colours on your page with this eye dropper.',
                        },
                        {
                            'name': 'JSON Formatter',
                        'url': 'https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa',
                        'intro':'Just like the name says, get help with your JSON issues.',
                        },
                        {
                            'name': 'Built With Technology Analyzer',
                        'url': 'https://chrome.google.com/webstore/detail/builtwith-technology-prof/dapjbgnjinbpoindlpdmhochffioedbn?hl=en-US',
                        'intro':'Lets you see what tools and JavaScript libraries a site is using.',
                        },
                        {
                            'name': 'Built With Technology Analyzer',
                        'url': 'https://chrome.google.com/webstore/detail/builtwith-technology-prof/dapjbgnjinbpoindlpdmhochffioedbn?hl=en-US',
                        'intro':'Lets you see what tools and JavaScript libraries a site is using.',
                        },
                        {
                            'name': 'Built With Technology Analyzer',
                        'url': 'https://chrome.google.com/webstore/detail/builtwith-technology-prof/dapjbgnjinbpoindlpdmhochffioedbn?hl=en-US',
                        'intro':'Lets you see what tools and JavaScript libraries a site is using.',
                        },
                        {
                            'name': 'Built With Technology Analyzer',
                        'url': 'https://chrome.google.com/webstore/detail/builtwith-technology-prof/dapjbgnjinbpoindlpdmhochffioedbn?hl=en-US',
                        'intro':'Lets you see what tools and JavaScript libraries a site is using.',
                        }
                    ]
]




Graphic_deginer = [
        {
        'id': 0,
        'image': 'https://speckyboy.com/wp-content/uploads/2019/02/free-adobe-premier-pro-video-templates-01.jpg',
        'intro': "Video is a great way to build trust with potential clients, showcase your products in use, and add a touch of personality to your brand. But if you want to achieve results with video marketing, you need to make sure your videos stand out from the competition.",
        'sum+up': "Free motion graphic templates",
        'name': 'speckybou',
        'url': 'https://speckyboy.com/free-templates-adobe-premier-pro/',
    },
    {
        'id': 0,
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/ira-design.jpg',
        'intro': "Ira Design is a free and open-source illustration tool developed by Creative Tim that help designers to build their own amazing illustrations using awesome gradients and hand-drawn sketch components.",
        'sum+up': "Free motion graphic templates",
        'name': 'Ira Design ',
        'url': 'https://iradesign.io/?ref=creativetim',
    },
    {
        'id': 0,
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/stubborn-generator-768x576.png',
        'intro': "Stubborn is a generator for customizable illustrations that can help you:",
        'sum+up': "illustration creator",
        'name': 'stburn generator',
        'url': 'https://stubborn.fun/',
    },
    {
        'id': 0,
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/vector-creator-768x480.jpeg',
        'intro': "Vector Illustration Creator is a free tool for creating illustrations with no need for design teamwork.",
        'sum+up': "Illustartion creator",
        'name': 'Vector Illustration Creator',
        'url': 'https://icons8.com/vector-creator',
    },
    {
        'id': 0,
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/unnamed-file-768x363.jpg',
        'intro': "Gravit Designer is a full-featured, vector graphic design solution for designers. The program provides a set of powerful tools that help the user to unleash true creativity in designing beautiful and detailed vector imagery. It is suitable for:",
        'sum+up': "Free motion graphic templates",
        'name': 'Gravit designer',
        'url': 'https://www.designer.io/en/',
    },
    {
        'id': 0,
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/smash-768x403.png',
        'intro': "Smash Illustration Is a very nice free illustration constructor that offers more than 250 illustrations ready to help you create unique scenes.",
        'sum+up': "Free motion graphic templates",
        'name': 'Smash Illustration ',
        'url': 'https://usesmash.com/',
    },
]


Machine_learning = [
    
]
gameDevelopment = [
    
]
Ui_Ux = [
    {
'id': 1,
'image':'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5c5957de3e262c46a81b4611_Artboard%2BCopy-p-1600.png',
'intro': 'Slick mockup movies and images for promo videos, presentations, portfolios, app store images.Showcasing like the big boys is no longer just for the big boys.',
'name': 'Rotato',
'url':'https://www.rotato.xyz/',
'extra': 'mockups',
'price': 'half free'
    },
    {
'id': 2,
'image': 'https://miro.medium.com/max/1600/1*oxxU6j6GXYODNT2is-KU6Q.gif',
'intro': 'Bring your apps and games to life with real-time animation. Rive is a powerful design and animation tool, which allows designers and developers to easily',
'name': 'rive 2',
'url':'https://www.2dimensions.com/',
'extra': 'animation',
'price': 'free'
    },
    {
        'id': 3,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5bf6e0c690b6c76a53804bdc_answers_calculator.png',
'intro': 'Understand how users are really experiencing your site without drowning in numbers Traditional web analytics tools help you analyze traffic data. But numbers alone can’t tell you what users really do on your site — Hotjar will.',
'name': 'hotjar',
'url':'https://www.hotjar.com/?utm_expid=.EinRyQaiRjGYjFEJFTUl4Q.0&utm_referrer=',
'extra': 'analytics',
'price': 'paid'
    },
    {
        'id': 4,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5be9b020d015a1f9ec9a5442_banner-2.png',
'intro': 'Are you working with design files? Start saving time today.In all plans you can present, comment, create screen flows, and inspect Sketch, Adobe XD, Photoshop, Illustrator, & Figma files - using our web, macOS, Windows, & Linux app',
'name': 'Avocode',
'url':'https://avocode.com/hand-off-and-inspect',
'extra': 'UI/UX designing',
'price': 'paid'
    },
    {
        'id': 5,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5bc453b95a68ee5fe21bc6b4_Screen%20Shot%202018-10-15%20at%2010.45.18%20AM.png',
'intro': 'Are you working with design files? Start saving time today.In all plans you can present, comment, create screen flows, and inspect Sketch, Adobe XD, Photoshop, Illustrator, & Figma files - using our web, macOS, Windows, & Linux app',
'name': 'micro',
'url':'https://realtimeboard.com/',
'extra': 'team collaboration for brainstroming + video call',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5ba39a9e805bfa74a4b08ddf_1_F19-hrmAQppP33zh1G2jgQ-p-1600.png',
'intro': 'To empower the work of design teams by facilitating a creative synergy through effortless collaboration.',
'name': 'plant',
'url':'https://plantapp.io/#about',
'extra': 'team collaboration for brainstroming + video call',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b866b1515ad26e6cea79353_2017-character_personas.jpg',
'intro': 'Generate professional, customizable buyer persona documents with the help of this quick and intuitive generator.',
'name': 'Make my persona',
'url': 'https://www.hubspot.com/make-my-persona',
'extra': 'personal portfolio',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b769ac79183f17ee9fe0942_by%20Norde.png',
'intro': 'Vaadin comes with a big set of web components that are fine-tuned for UX, performance, and accessibility.',
'name': 'vaadin',
'url':'https://vaadin.com/',
'extra': 'web apps => java',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b583ac6fc79dd91ac4f68af_30134265966479.5b075bbf1b0a7.jpg',
'intro': 'Discover how real users interact with your prototype: define missions, collect actionable insights and analyze how your design performed, with 0 lines of code.',
'name': 'maze',
'url':'https://maze.design/',
'extra': 'ui/ux testing + analytics for prototypes',
'price': 'free 1 month trial'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b3c86048d4e3381013434c0_color-tool-v2-4x3.gif',
'intro': 'The Material Theme Editor helps you make your own branded symbol library and apply global style changes to color, shape, and typography.',
'name': 'gallery',
'url':'https://gallery.io/apps',
'extra': 'matrial theme editor',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5afb0c4a5d83d9375a8d19d0_social_tout.png',
'intro': "By choosing a set of 50 colors, you'll train a neural network powered algorithm to generate colors you like and block ones you don’t, right in your browser.",
'name': 'khroma',
'url':'http://khroma.co/',
'extra': 'Design with colors you love. Khroma uses AI to learn which colors you like and creates limitless palettes for you to discover, search, and save.',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5ac3825ee45951aaec5936b0_homepage-bg-669c8ea95a9ede671933dffb254f493a23de2d7a039f90bfbbac9ecd09f78225.svg',
'intro': 'Share your ideas visually. Lightning fast.',
'name': 'gallery',
'url':'https://whimsical.co/',
'extra': 'brainstrming workspace',
'price': 'create 4 free boards '
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5a5dc7eb3e2b760001e215f4_Illustration%20by%20Iza%20Dudzik.jpg',
'intro': 'Piece hi-fi interactions together, build sensor-aided prototypes and share your amazing creations in a matter of minutes.',
'name': 'protopie',
'url':'https://www.protopie.io/',
'extra': 'prototyping tool',
'price': 'free for students'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5a312b470672a700015a499c_brics.gif',
'intro': 'Blocs Website Builder Fast, easy to use and powerful visual web design software, that lets you create responsive websites without writing code.',
'name': 'blocs',
'url':'https://blocsapp.com/',
'extra': 'websitebuilder',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9cb80a71c7d00019122e2_lottie.png',
'intro': 'Lottie is an iOS, Android, and React Native library that renders After Effects animations in real time, allowing apps to use animations as easily as they use static images.',
'name': 'lottie',
'url':'https://lottiefiles.com/getting-started#',
'extra': 'animation maker',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9c715775aae00019a177c_monotype-library-subscription_lead-image-p-1600.jpeg',
'intro': 'With more than 2,200 font families all in one location, you can easily find the perfect typeface for your project. Whether it’s for your own, a client’s or your company’s design, having complete access to a broad selection of high-quality, premium type is a must.',
'name': 'monotype library',
'url':'https://blocsapp.com/',
'extra': 'fonts',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e8a73a90983b000144f01e_webflow.png',
'intro': 'The modern way to build for the web Webflow empowers designers to build professional, custom websites in a completely visual canvas. View dashboard',

'name': 'webflows',
'url':'https://webflow.com/',
'extra': 'websitebuilder',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e215007032510001bb636f_home-screenshot.png',
'intro': "Online app that enables designers to customize their own typeface in a few clicks.",
'name': 'prototypo',
'url':'https://www.prototypo.io/',
'extra': 'fonts',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e218ae3f6bfa0001113de7_invision-logo.jpg',
'intro': "The world's leading prototyping, collaboration & workflow platform",
'name': 'invision',
'url':'https://www.invisionapp.com/',
'extra': 'prototyping + devlopment fro m design',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Adobe_XD_CC_icon.svg/1200px-Adobe_XD_CC_icon.svg.png',
'intro': "Share your story with designs that look and feel like the real thing. Wireframe, animate, prototype, collaborate and more — it’s all right here, all in one place.",
'name': 'Adobe xd',
'url':'https://www.adobe.com/in/products/xd.html',
'extra': 'ui/ux designing',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5c59570b4abddd53b41de8a2_marginalia-productive-work.png',
'intro': "1000+ Pixel-perfect vector icons and Iconfont for your next project.",
'name': 'icons',
'url':'http://s.muz.li/ZTg1MWRhOTJk',
'extra': 'ui/ux designing',
'price': 'free',
'type': 'Resources'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5c33558eedb5fd1b94b42c45_pablo-delete-confirmation.png',
'intro': "Email copy from great companies. Brought to you by Front.",
'name': 'email copy',
'url':'https://www.goodemailcopy.com/',
'extra': 'all mail in one place',
'price': 'free',
'type': 'Resources'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5be9af7bd91668e74ade48ab_form-feature-copy-min-810x810.jpg',
'intro': "Meet Form, an intuitive wireframe kit that will help you hit the ground running with your next design project.",
'name': 'form',
'url':'https://www.invisionapp.com/inside-design/design-resources/free-wireframe-kit-form/',
'extra': 'form',
'price': 'free',
'type': 'Resources'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b9f720f08470e3f35fac2cd_undraw_upload_87y9%20(1).svg',
'intro': "Browse to find the images that fit your needs and click to download. Take advantage of the on-the-fly color image generation to match your brand identity.",
'name': 'UnDraw',
'url':'https://undraw.co/illustrations',
'extra': 'Illustartions',
'price': 'free',
'type': 'Resources'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5ba399a0d65e6ec06564fe74_undraw_High_five_u364.svg',
'intro': "Are you looking for blend mode background images & beautiful background gradients for your User Interface?",
'name': 'Gradient guru',
'url':'http://gradientsguru.com/',
'extra': 'Gradients',
'price': 'free',
'type': 'Resources'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5ace6ff8507eccc0c1b1d2d6_solareclipse.gif',
'intro': "A total set of 14 color palettes and 280 colors for your designs, projects, presentations and other needs.",
'name': 'flat ui color',
'url':'https://flatuicolors.com/',
'extra': 'colors pallets',
'price': 'free',
'type': 'Resources'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5a13ef322d9bd30001824403_wallpaper_concert-2.png',
'intro': "Upload your design, adjust settings and download your individual mockup. Threed is for free and needs no extra Software",
'name': 'Threed',
'url':'http://threed.io/',
'extra': 'Generate 3d mockups in browser',
'price': 'free',
'type': 'Resources'
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5c05205a90375ebb9d52fad7_Image-p-1600.jpeg',
        'into': 'Mix-&-match illustrations of people with a design library',
        'name': 'Hummans',
        'url': 'https://www.humaaans.com/?ref=producthunt',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5bf6e3d14ae3421f52814444_download.jpg',
        'into': 'Mobbin is a hand-picked collection of the latest mobile design patterns from apps that reflect the best in design. Get inspiration from over 150 iOS apps and 8,000 patterns (screenshots from iPhone X) available on the platform. Sign up to save your favorite patterns.',
        'name': 'mobbin',
        'url': 'https://mobbin.design/',
        'extra': 'ios design pattrens',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59fc7d4b605d4b0001f003e9_marriot_copy.jpg',
        'into': 'Take responsive screenshots with the click of button',
        'name': 'Responsive screenshorts',
        'url': 'https://responsive-screenshots.com/',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "Resource",
    },
    
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5c05205a90375ebb9d52fad7_Image-p-1600.jpeg',
        'into': 'Mix-&-match illustrations of people with a design library',
        'name': 'Hummans',
        'url': 'https://www.humaaans.com/?ref=producthunt',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9bea6e87a4d000109dbd1_jakub-dziubak-394720-(1).jpg',
        'into': 'Beautiful high quality free images and photos you can download and use for any project. No attribution required.',
        'name': 'unsplash',
        'url': 'https://unsplash.com/',
        'extra': 'Photos',
        'price': 'free',
        'type': "Resource",
    },
    
    {
        'id': 0,
        'image': 'https://www.logo-designer.co/wp-content/uploads/2013/09/iStock-logo-design-identity-getty-images-Build.jpg',
        'into': 'free photos',
        'name': 'istock',
        'url': 'https://www.istockphoto.com/collaboration/boards/L9m43WDlbUO8O94wqUFIIA',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://cdn.joypixels.com/sections/coverphotos/6.0%20Release%20FINAL%20FINAL-02-min.png',
        'into': 'New for 2020! JoyPixels 6.0 includes 3,342 originally crafted icon designs and is 100% Unicode 13 compatible. We offer the largest selection of files ranging from png, svg, iconjar, sprites, and fonts.',
        'name': 'PIXELS',
        'url': 'https://www.joypixels.com/',
        'extra': 'Emoji',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://static-cdn.pixlr.com/images/pixlr-header-logo.png',
        'into': 'Pixlr, the World’s Favorite #1 Online Photo Editor lets you edit photos right in your browser for Free. Experience next level, intuitive photo editing with AI-powered tools for quick yet professional edits',
        'name': 'PIXLR',
        'url': 'https://www.joypixels.com/',
        'extra': 'Emoji',
        'price': 'free',
        'type': "Resource",
    },
]

android = [
            {
                'id': 6,
'image': 'https://blog.stylingandroid.com/wp-content/uploads/2016/10/banner-Oct-2016.png',
'intro': "1000+ Pixel-perfect vector icons and Iconfont for your next project.",
'name': 'Material Motion: Container Transform',
'url':'https://blog.stylingandroid.com/',
'extra': 'Android',
'price': 'free',
'type': 'Resources'
            },
            {
        'id': 0,
        'image': 'https://giphy.com/static/img/giphy_logo_square_social.png',


        'intro': 'GIPHY is your top source for the best & newest GIFs & Animated Stickers online. Find everything from funny GIFs, reaction GIFs, unique GIFs and more',


        'intro': 'GIPHY is your top source for the best & newest GIFs & Animated Stickers online. Find everything from funny GIFs, reaction GIFs, unique GIFs and more',

        'name': 'giphy.com',
        'url': 'https://giphy.com/',
        'extra': 'Giphy',
        'price': 'free',
        'type': "gifs",
    },
        ]



@tools.route('/programming/tools')
def api_programming_tools():
    return jsonify(programming)
@tools.route('/Ui_Ux/tools')
def api_Ui_Ux_tools():
    return jsonify(Ui_Ux)
@tools.route('/gameDevelopment/tools')
def api_gameDevelopment_tools():
    return jsonify(gameDevelopment)
@tools.route('/Graphic_deginer/tools')
def api_Graphic_deginer_tools():
    return jsonify(Graphic_deginer)
@tools.route('/webDevelopment/tools')
def api_webDevelopment_tools():
    return jsonify(webDevelopment)
@tools.route('/android/tools')
def api_webDevelopment_tools():
    return jsonify(android)
@tools.route('/Machine_learning/tools')
def api_Machine_learning_tools():
    return jsonify(Machine_learning)
