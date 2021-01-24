

from flask import Flask, request, jsonify


app = Flask(__name__)
app.config["DEBUG"] = True



# Create some test data for our catalog in the form of a list of dictionaries.
all_resources = [
    {
        'name': 'podcasts',
        'url': 'https://edu-link-api.herokuapp.com/podcasts'
        
    }
    ,
    {
        'name': 'must programmer',
        'url': 'https://edu-link-api.herokuapp.com/mustprogrammer',
        "tools" : 'https://edu-link-api.herokuapp.com/mustprogrammer/tools',
        "courses": 'https://edu-link-api.herokuapp.com/mustprogrammer/courses',
        "learnin": 'https://edu-link-api.herokuapp.com/mustprogrammer/learning',
    }
    ,
    {
        'name': 'gameDevelopment',
        'url': 'https://edu-link-api.herokuapp.com/gameDevelopment',
        "tools" : 'https://edu-link-api.herokuapp.com/gameDevelopment/tools',
        "courses": 'https://edu-link-api.herokuapp.com/gameDevelopment/courses',
        "learnin": 'https://edu-link-api.herokuapp.com/gameDevelopment/learning',
    }
    ,
    {
        'name': 'programming',
        'url': 'https://edu-link-api.herokuapp.com/programming',
        "tools" : 'https://edu-link-api.herokuapp.com/programming/tools',
        "courses": 'https://edu-link-api.herokuapp.com/programming/courses',
        "learnin": 'https://edu-link-api.herokuapp.com/programming/learning',
    }
    ,
    {
        'name': 'webDevelopment',
        'url': 'https://edu-link-api.herokuapp.com/webDevelopment',
        "tools" : 'https://edu-link-api.herokuapp.com/webDevelopment/tools',
        "courses":'https://edu-link-api.herokuapp.com/webDevelopment/courses',
        "learnin": 'https://edu-link-api.herokuapp.com/webDevelopment/learning',
    }
    ,
    {
        'name': 'webdesigner',
        'url': 'https://edu-link-api.herokuapp.com/webdesigner',
        "tools" : 'https://edu-link-api.herokuapp.com/webdesigner/tools',
        "courses": 'https://edu-link-api.herokuapp.com/webdesigner/courses',
        "learnin": 'https://edu-link-api.herokuapp.com/webdesigner/learning',
    }
    ,
    {
        'name': 'androiddevelopment',
        'url': 'https://edu-link-api.herokuapp.com/android',
        "tools" : 'https://edu-link-api.herokuapp.com/android/tools',
        "courses": 'https://edu-link-api.herokuapp.com/android/courses',
        "learnin": 'https://edu-link-api.herokuapp.com/android/learning',
    }
    ,
    {
        'name': 'Machine_learning',
        'url': 'https://edu-link-api.herokuapp.com/Machine_learning',
        "tools" : 'https://edu-link-api.herokuapp.com/Machine_learning/tools',
        "courses": 'https://edu-link-api.herokuapp.com/Machine_learning/courses',
        "learnin": 'https://edu-link-api.herokuapp.com/Machine_learning/learning',
    }
    ,
    {
        'name': 'Ui_Ux',
        'url': 'https://edu-link-api.herokuapp.com/Ui_Ux',
        "tools" : 'https://edu-link-api.herokuapp.com/Ui_Ux/tools',
        "courses": 'https://edu-link-api.herokuapp.com/Ui_Ux/courses',
        "learnin": 'https://edu-link-api.herokuapp.com/Ui_Ux/learning',
    }
    ,
    {
        'name': 'freecourses',
        'url': 'https://edu-link-api.herokuapp.com/freecourses',
    },
    {
        'name': 'animationimage',
        'url': 'https://edu-link-api.herokuapp.com/animationimage',
    }
    ,
    {
        'name': 'font',
        'url': 'https://edu-link-api.herokuapp.com/font',
    }
    ,
    {
        'name': 'color',
        'url': 'https://edu-link-api.herokuapp.com/color',
    }
    ,
    {
        'name': 'music',
        'url': 'https://edu-link-api.herokuapp.com/musicassets',
    }
    ,
    {
        'name': 'Awesome tools',
        'url': 'https://edu-link-api.herokuapp.com/checkout_tools',
    }
    ,
    {
        'name': 'graphicdesigner',
        'url': 'https://edu-link-api.herokuapp.com/graphicdesigner',
    }
    ,
    {
        'name': 'freebooks',
        'url': 'https://edu-link-api.herokuapp.com/freebooks',
    }
    ,
    {
        'name': 'freecourses',
        'url': 'https://edu-link-api.herokuapp.com/freecourses',
    }
    ,
    {
        'name': 'freesoftware',
        'url': 'https://edu-link-api.herokuapp.com/freesoftware',
    }
    ,
    {
        'name': 'youtubechannels',
        'url': 'https://edu-link-api.herokuapp.com/youtubechannels',
    }
    ,
    {
        'name': 'Bonus(New)',
        'url': 'https://edu-link-api.herokuapp.com/youtubechannels',
    },
    {
        'name': 'everyydaytools',
        'url': 'https://edu-link-api.herokuapp.com/everyydaytools',
    },
    {
        'name': 'freedeveloperasstes',
        'url': 'https://edu-link-api.herokuapp.com/freedeveloperasstes',
    },
    {
        'name': 'logo',
        'url': 'https://edu-link-api.herokuapp.com/logo',
    },
    {
        'name': 'articles',
        'url': 'https://edu-link-api.herokuapp.com/articles',
    }
    ,
    {
        'name': 'motivation',
        'url': 'https://edu-link-api.herokuapp.com/motivation',
    }
] 
motivation = [
    {

    }
]


Podcasts = [
    {
        
     'image': 'https://pbs.twimg.com/profile_images/1143571889681588224/zGPH4uEj.png',
     'intro': 'General career advice for beginner to intermediate-level coders.',
     'type':'website ComputerScience',
     'name': 'No BS Engineering',
     'url': 'https://nobsengineering.com/'
    },
    {
        
     'image': 'https://s3.amazonaws.com/heroku-www-files/podcasts/uploads/software_engineering_daily.png',
     'intro': 'Software development topics including technical interviews.',
     'type':'website ComputerScience',
     'name': 'Software Engineering daily',
     'url': 'https://softwareengineeringdaily.com/'
    },
    {
        
     'image': 'https://s3.amazonaws.com/codenewbie-assets/basecs+podcast+cover+7+small.png',
     'intro': 'Beginner-friendly computer science lessons based on Vaidehi Joshi’s base.cs blog series, produced by CodeNewbie.',
     'type':'website ComputerScience',
     'name': 'Base.cs Podcast',
     'url': 'https://www.codenewbie.org/basecs'
    },
    {
        
     'image': 'https://files.realpython.com/media/Real-Python-Podcast_BLUE_Waterkmarked.b5ff55c349bd.jpg',
     'intro': 'A weekly Python podcast hosted by Christopher Bailey with interviews, coding tips, and conversation with guests from the Python community. The show covers a wide range of topics including Python programming best practices, career tips, and related software development topics',
     'type':'websites Python',
     'name': 'Real Python Talk',
     'url': 'http://ebuaccesscast.libsyn.com/'
    },
    {
        
     'image': 'https://i.ytimg.com/vi/Tlf4JWiZVFA/maxresdefault.jpg',
     'intro': 'Every week a new episode provides useful and informative insights into the projects, platforms, and practices that engineers, business leaders, and data scientists need to know about to learn and grow in their career.',
     'type':'websites Python',
     'name': 'pythonpodcast',
     'url': 'https://www.pythonpodcast.com/'
    },
    {
        
     'image': 'https://pbcdn1.podbean.com/imglogo/dir-logo/327316/327316_300x300.png',
     'intro': 'If you are looking for a 15 minute conversation on the topical items of the week in the Python ecosystem, be sure to jump over to Python Bytes.',
     'type':'websites',
     'name': 'Python Bytes',
     'url': 'https://pythonbytes.fm/'
    },
    {
        
     'image': 'https://talkpython.fm/static/img/talk_python_logo_mic.png',
     'intro': 'The show covers a wide array of Python topics as well as many related topics (e.g. MongoDB, AngularJS, DevOps). The format is a casual 45 minute conversation with industry experts.',
     'type':'websites',
     'name': 'Talk Python To Me',
     'url': 'https://talkpython.fm/'
    },
    {
        
     'image': 'https://darknetdiaries.com/imgs/darknet-diaries-sm.jpg',
     'intro': 'InfoSec / CyberSecurity Darknet Diaries is a podcast covering true stories from the dark side of the Internet. Stories about hackers, defenders, threats, malware, botnets, breaches, and privacy',
     'type':'websites InfoSec / CyberSecurity',
     'name': 'Darknet Diaries',
     'url': 'https://darknetdiaries.com/'
    },
    {
        
     'image': 'https://s3.amazonaws.com/devchat.tv/viewsonvue.jpg',
     'intro': 'A weekly discussion among Vue developers about Vue and it’s ecosyste',
     'type':'websites Vue (JavaScript framework)',
     'name': 'Views on Vue',
     'url': 'https://devchat.tv/views-on-vue/'
    },
    {
        
     'image': 'https://designm.ag/wp-content/uploads/2015/10/developer-tea.jpg',
     'intro': 'Provides advice and tips on becoming a better developer.',
     'type':'websites Mindset/Self-Development',
     'name': 'Developer Tea',
     'url': 'https://spec.fm/podcasts/developer-tea'
    },
    {
        
     'image': 'https://www.devshows.dev/static/d376585cbfb41ab6eb4ef65daaa17e2b/c972b/js-party.png',
     'intro': 'A community celebration of JavaScript and the web. Created by the Changelog Developer Community. It records live every Thursday at 1 pm Eastern / 10 am Pacific U.S. time.',
     'type':'websites','name': 'JS Party',
     'url': 'https://changelog.com/jsparty'
    },
    {
        
     'image': 'https://i.ytimg.com/vi/V2P7pC3e-_M/maxresdefault.jpg',
     'intro': 'Julia Ferraioli says if you’re already dealing with blurry vision, making something blurry bigger, isn’t necessarily going to help that much.',
     'type':'websites','name': 'A11y Rules',
     'url': 'https://a11yrules.com/'
    },
    {
     'image': 'https://miro.medium.com/max/1000/1*c4KOwhSRiE53ril7PQg2ow.png',
     'intro': 'We are a few guys who’ve been professional programmers for years. As avid listeners of podcasts and consumers of many things code-related, we were frustrated by the lack of quality programming (pun) available in listenable formats. Given our years of experience and real-world problem-solving skills, we thought it might be worth getting intro this world of podcasting and “giving back” a shot.',
     'type':'websites','name': 'Coding Blocks',
     'url': 'https://www.codingblocks.net/'
     },
    {
     'image': 'https://spec.fm/static/img/shows/developertea.jpg',
     'intro' : "In January 2015, two independent podcasts — Design Details and Developer Tea — were started by three individuals who wanted to talk about the work they do every day. After an amazing response from the web community, we’ve teamed up to create the Spec Network to help designers and developers to learn, find great resources and connect with one another.",
     'type':'websites','name': 'Developer Tea',
     'url': 'https://spec.fm/podcasts/developer-tea'
     },
    {'id': 2,
     'image': 'https://fullstackradio.com/podcast-cover.jpg',
     'intro': 'A podcast for developers interested in building great software products. Every episode, Adam Wathan is joined by a guest to talk about everything from product design and user experience to unit testing and system administration.',
     'type':'websites','name': 'Full Stack Radio',
     'url': 'https://fullstackradio.com/'
     },
    {
        'id': 4,
        'image':    'https://ssl-static.libsyn.com/p/assets/2/f/f/7/2ff7cc8aa33fe438/freecodecamp-square-logo-large-1400.jpg',
        'intro':'The official podcast of the freeCodeCamp open source community. Learn to code with free online courses, programming projects, and interview preparation for developer jobs.',
        'type':'websites','name': 'freeCodeCamp podcast',
        'url': "https://freecodecamp.libsyn.com/",
    },
    {
        'id': 5,
        'image':    'https://miro.medium.com/max/3200/1*op8UQr4cvuoQEdPSiyO8zQ.jpeg',
        'intro':    'React Native Radio. Exploring React Native Together. Listen & Subscribe. Recent Episodes. RNR 185 - Navigation with Graham Mendick. In this episode, the',
        'type':'websites','name': 'reactnativeradio',
        'url': 'https://reactnativeradio.com/',
    },
    {
        'id': 5,
        'image':    'https://syntax.fm/static/syntax-banner.png',
        'intro':    'The amazing Wes Bos & Scott Tolinksi hosts a podcast covering web development, front-end, the process of learning, and business. You can also find their episodes on various apps like Spotify etc.',
        'type':'websites',
        'name': 'Syntax.fm',
        'url': 'https://syntax.fm/',
    },
     {
        'id': 5,
        'image':    'https://s3.amazonaws.com/devchat.tv/reactroundup.jpg',
        'intro':    'On this episode of React Round Up we talked to Dragos Bulugean about starting your own business, and managing really big apps.',
        'type':'websites',
        'name': 'reactroundup',
        'url': 'https://devchat.tv/podcasts/react-round-up/',
    },
     {
        'id': 5,
        'image':    'https://media.simplecast.com/episode/image/324092/thumb_1602263739-artwork.jpg',
        'intro':    'The Laracasts Snippet, each episode, offers a single thought on some aspect of web development. Nothing more, nothing less. Hosted by Jeffrey Way.',
        'type':'websites',
        'name': 'Real Talk JavaScript',
        'url': 'https://webrush.simplecast.com/',
    },
     {
        'id': 5,
        'image':    'https://media.simplecast.com/episode/image/324092/thumb_1602263739-artwork.jpg',
        'intro':    'The Laracasts Snippet, each episode, offers a single thought on some aspect of web development. Nothing more, nothing less. Hosted by Jeffrey Way.',
        'type':'websites',
        'name': 'the laracasts snippet',
        'url': 'https://laracasts.simplecast.fm/',
    },
     {
        'id': 5,
        'image':    'https://media.simplecast.com/episode/image/324092/thumb_1602263739-artwork.jpg',
        'intro':    'The Laracasts Snippet, each episode, offers a single thought on some aspect of web development. Nothing more, nothing less. Hosted by Jeffrey Way.',
        'type':'websites',
        'name': 'the laracasts snippet',
        'url': 'https://laracasts.simplecast.fm/',
    },
     {
        'id': 5,
        'image':    'https://media.simplecast.com/episode/image/324092/thumb_1602263739-artwork.jpg',
        'intro':    'The Laracasts Snippet, each episode, offers a single thought on some aspect of web development. Nothing more, nothing less. Hosted by Jeffrey Way.',
        'type':'websites',
        'name': 'the laracasts snippet',
        'url': 'https://laracasts.simplecast.fm/',
    },
     {
        'id': 5,
        'image':    'https://media.simplecast.com/episode/image/324092/thumb_1602263739-artwork.jpg',
        'intro':    'The Laracasts Snippet, each episode, offers a single thought on some aspect of web development. Nothing more, nothing less. Hosted by Jeffrey Way.',
        'type':'websites',
        'name': 'the laracasts snippet',
        'url': 'https://laracasts.simplecast.fm/',
    },
]
Must_programmer_main = [
    {
        'name':'programmingmain',
        'start':[
            {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/33tbBpGanLQYMSxpnkL7nC/02bc0ffd5053dd8b0b146faa145f37f2/Git_Branching.PNG?w=800&h=387&q=50&fm=webp',
        'intro':'Coursera Course (Not CS Specific) teach you how the mind grasp thing and how to train it to learn things as convinient and fast as possible',
        'type':'websites','name': 'Learn Git Branching Interactively',
        'url': 'https://www.coursera.org/learn/learning-how-to-learn'
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/33tbBpGanLQYMSxpnkL7nC/02bc0ffd5053dd8b0b146faa145f37f2/Git_Branching.PNG?w=800&h=387&q=50&fm=webp',
        'intro':'The most visual, interactive and fun way to learn Git on the web.',
        'type':'websites','name': 'Learn Git Branching Interactively',
        'url': 'https://learngitbranching.js.org/'
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5qFgoOTACYlbYpc2pPlqjM/a0f2662b4e2a3bfc2fc30c84b7f6e963/1500x500?w=800&h=267&q=50&fm=webp',
        'intro':'Find the right git commands you need without digging through the web.',
        'type':'websites','name': 'Git Command Explorer',
        'url': 'https://gitexplorer.com/'
    },

    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5qFgoOTACYlbYpc2pPlqjM/a0f2662b4e2a3bfc2fc30c84b7f6e963/1500x500?w=800&h=267&q=50&fm=webp',
        'intro':'Free individual licenses of the award-winning professional developer tools from JetBrains for students and faculty members.',
        'type':'websites','name': 'JetBrains Student License',
        'url': 'https://www.jetbrains.com/student/'
    },
    


    
    {
        'id': 0,
        'image': 'https://github.blog/wp-content/uploads/2014/10/4b0317bc-4599-11e4-8bc3-0ca4dd5223e8.png?resize=2284%2C889',
        'intro':'There’s no substitute for hands-on experience, but for most students, real world tools can be cost prohibitive. That’s why github created the GitHub Student Developer Pack with some of there partners and friends: to give students free access to the best developer tools in one place so they can learn by doing',
        'type':'websites','name': 'GitHub Student Developer Pack',
        'url': 'https://education.github.com/'
    },
    {
        'id': 0,
        'image': 'https://149351115.v2.pressablecdn.com/wp-content/uploads/2017/02/college-degrees-1024x395.jpg',
        'intro':'Do developers need college degrees? Just a generation ago, it was a given that a college degree was the best way to maximize the likelihood of securing a high-paying job in the field of your choice. But the world has changed, and more and more you hear of successful developers who never earned a degree,',
        'type':'websites','name': 'Do Developers Need College Degrees?',
        'url': 'https://stackoverflow.blog/2016/10/07/do-developers-need-college-degrees/?fbclid=IwAR1H9tBaYd1zGUIam6nVQovHcJETHwoo11VHBlV8peR0JO8PJNgAHMsQqvw'
    },
    {
                'id':0,
        'image': 'https://online-learning.harvard.edu/sites/default/files/styles/social_share/public/course/cs50x-original.jpg?itok=kR_JV8DW',
        'intro': 'An entry-level course taught by David J. Malan, CS50x teaches students how to think algorithmically and solve problems efficiently.',
        'type':'websites','name': 'cs50',
        'Return': 'free certificate',
        'url':  'https://www.edx.org/course/cs50s-introduction-to-computer-science'
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/6YUQllDI9KrCgiZy8GsMnZ/c38322baa2bfc2d8af1f6ca19ae6e564/maxresdefault.jpg?w=800&h=450&q=50&fm=webp',
        'intro':'This tutorial will teach you modern git and Github',
        'type':'websites','name': 'In Depth Tutorial on Git & Github (DevOps Tools)',
        'url': 'https://www.youtube.com/watch?v=6bjCvZEX52w'
    },
    {
        'id': 0,
        'image': 'https://pr.azureedge.net/img/picresize_logo_registered.png',
        'intro': "visual representaiton of Diffrent Algorithms",
        'type':'websites','name': 'Visual Algo',
        'url': 'https://visualgo.net/en',
    }
    ,
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/6lslLWTrtJOvT9uKL76BdA/c68fa37469f4052acc66944843ba310a/image.png?w=300&h=168&q=50&fm=webp',
        'intro': "Better understand how far computers have taken us and how far they may carry us.",
        'type':'websites','name': 'Crash Course Computer Science',
        'url': 'https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo',
    }
    ,
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/2MdYGTNWLQ4qpBn9lv6Npy/700fed96c05f8149567c70aa871f9bd7/maxresdefault.jpg?w=800&h=450&q=50&fm=webp',
        'intro': "The latest edition of the fantastic, free computer science lectures from Harvard.",
        'type':'websites','name': 'Cs50 2020',
        'url': 'https://youtu.be/Tpl7k8IOT6E',
    }
        ]
    },
    {'programming_tools' : [
            
    {
        'id': 0,'type':'website',
        'image': 'https://images.ctfassets.net/aq13lwl6616q/4tfKlG1Ylr94FeVUQH5Oic/2bfef3e8d5536a47e52e6e5f50c258c8/og-square.png?w=640&h=640&q=50&fm=webp',
        'intro': "An interactive map of popular screen sizes showing the responsive and adaptive device landscape",
        'name': 'Screen Size Map',
        'url': 'https://www.screensizemap.com/',
    }
    ,
    {
        'id': 0,'type':'website',
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5FX7FgtToDupaRBZuRFW3m/3e822bfe48221fe462ba9205ead4be9b/image.png',
        'intro': "Automatically remove an image background with no clicks and for free in 5 seconds.",
        'name': 'Image Background Remover',
        'url': 'https://www.remove.bg/',
    },
    {
        'id': 0,'type':'website',
        'image': 'https://images.ctfassets.net/aq13lwl6616q/3D1UOB3RrnRLcTtMytmyJa/284a58d52a99d52ded174c17790daeb8/image.png?w=800&h=421&q=50&fm=webp',
        'intro': "Create and share beautiful images of your source code.",
        'name': 'Codeimg.io',
        'url': 'https://codeimg.io/',
    },
    {
        'id': 0,'type':'website',
        'image': 'https://images.ctfassets.net/aq13lwl6616q/2SSyh2voG8mIcUlkpNDDbp/850fa97bd0d109fb16e318edbbfaa7db/image.png',
        'intro': "Free online tools for bulk image processing (resize, crop, compress and more).",
        'name': 'Bulk Image Processing',
        'url': 'https://www.imgbot.ai/',
    },
    {
        'id': 0,'type':'website',
        'image': 'https://images.ctfassets.net/aq13lwl6616q/71B5MfU2Oe5l9BNITmQYYi/ca1fd6bf70dbbf19879648232f4f2497/screenshot.png?w=800&h=450&q=50&fm=webp',
        'intro': "Develop responsive web apps 5x faster. A must-have DevTool for all Front-End developers that will ma",
        'name': 'Responsively',
        'url': 'https://responsively.app/',
    },
    {
        'id': 0,'type':'website',
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5UJgTMBsuDqpV1JVgOryvn/59e8e7289d63ba2cd2c6eb884f18014b/image.png?w=304&h=166&q=50&fm=webp',
        'intro': "The most complete resource for the best monospace coding fonts.",
        'name': 'Programming Fonts',
        'url': 'https://app.programmingfonts.org/',
    },
    {
        'id': 0,'type':'website',
        'image': 'https://images.ctfassets.net/aq13lwl6616q/11n7eqjDE3UFlt5v6OkRBT/dd0beaf8e09dc2a61c651833f3ed553f/image.png?w=800&h=416&q=50&fm=webp',
        'intro': "A tool to debug and generate meta tag code for any website.",
        'name': 'Meta Tags',
        'url': 'https://metatags.io/',
    },
    {
        'id': 0,'type':'website',
        'image': 'https://images.ctfassets.net/aq13lwl6616q/4kVxycBS3keteNdBmEDsC8/abbd160757896407cd696c964719dfda/image.png?w=175&h=175&q=50&fm=webp',
        'intro': "Lorem Ipsum... but for photos.",
        'name': 'Lorem Picsum',
        'url': 'https://picsum.photos/',
    },
     {
        'id': 0,'type':'website',
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5iPXVJ2jpDKGyPyfcHhMJ9/36b7d3f8af92ab6703f94b6152e5c547/image.png?w=676&h=676&q=50&fm=webp',
        'intro': "Collection of open APIs (movies, weather, food, news, and more) for development",
        'name': 'Public APIs',
        'url': 'https://public-apis.xyz/',
    },
    {
        'id': 0,'type':'website',
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5b7A0ciaL5LU4wmb2ZYG0v/bb681d4a2c55c2b3c5aedb3479dda7e7/5aecb012-4bda-467c-9782-1ef157aec0d2?w=800&h=450&q=50&fm=webp',
        'intro': "Instantly resize and crop your photos & images for all web and social media formats with one click",
        'name': 'Free Image and Photo Resizer',
        'url': 'https://promo.com/tools/image-resizer/',
    },
    {
        'id': 0,'type':'website',
        'image': 'https://images.ctfassets.net/aq13lwl6616q/1YefYhckdPwmjhjvfUhsI7/c3371fb888864ad70bb0af1b40bf54de/image.png',
        'intro': "Use generative art for your image placeholders.",
        'name': 'Generative Placeholders',
        'url': 'https://generative-placeholders.glitch.me/',
    },
]
},
{
    'name': 'Must_programmer_courses',
    'start' : [
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/33tbBpGanLQYMSxpnkL7nC/02bc0ffd5053dd8b0b146faa145f37f2/Git_Branching.PNG?w=800&h=387&q=50&fm=webp',
        'intro':'Coursera Course (Not CS Specific) teach you how the mind grasp thing and how to train it to learn things as convinient and fast as possible',
        'type': 'website',
        'name': 'Learn Git Branching Interactively',
        'url': 'https://www.coursera.org/learn/learning-how-to-learn'
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/33tbBpGanLQYMSxpnkL7nC/02bc0ffd5053dd8b0b146faa145f37f2/Git_Branching.PNG?w=800&h=387&q=50&fm=webp',
        'intro':'The most visual, interactive and fun way to learn Git on the web.',
        'type': 'website + game',
        'name': 'Learn Git Branching Interactively',
        'url': 'https://learngitbranching.js.org/'
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5qFgoOTACYlbYpc2pPlqjM/a0f2662b4e2a3bfc2fc30c84b7f6e963/1500x500?w=800&h=267&q=50&fm=webp',
        'intro':'Find the right git commands you need without digging through the web.',
        'type': 'website',
        'name': 'Git Command Explorer',
        'url': 'https://gitexplorer.com/'
    },

    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5qFgoOTACYlbYpc2pPlqjM/a0f2662b4e2a3bfc2fc30c84b7f6e963/1500x500?w=800&h=267&q=50&fm=webp',
        'intro':'Free individual licenses of the award-winning professional developer tools from JetBrains for students and faculty members.',
        'type': 'website',
        'name': 'JetBrains Student License',
        'url': 'https://www.jetbrains.com/student/'
    },
    


    
    {
        'id': 0,
        'image': 'https://github.blog/wp-content/uploads/2014/10/4b0317bc-4599-11e4-8bc3-0ca4dd5223e8.png?resize=2284%2C889',
        'intro':'There’s no substitute for hands-on experience, but for most students, real world tools can be cost prohibitive. That’s why github created the GitHub Student Developer Pack with some of there partners and friends: to give students free access to the best developer tools in one place so they can learn by doing',
        'type': 'website',
        'name': 'GitHub Student Developer Pack',
        'url': 'https://education.github.com/'
    },
    {
        'id': 0,
        'image': 'https://149351115.v2.pressablecdn.com/wp-content/uploads/2017/02/college-degrees-1024x395.jpg',
        'intro':'Do developers need college degrees? Just a generation ago, it was a given that a college degree was the best way to maximize the likelihood of securing a high-paying job in the field of your choice. But the world has changed, and more and more you hear of successful developers who never earned a degree,',
        'type': 'website',
        'name': 'Do Developers Need College Degrees?',
        'url': 'https://stackoverflow.blog/2016/10/07/do-developers-need-college-degrees/?fbclid=IwAR1H9tBaYd1zGUIam6nVQovHcJETHwoo11VHBlV8peR0JO8PJNgAHMsQqvw'
    },
    {
                'id':0,
        'image': 'https://online-learning.harvard.edu/sites/default/files/styles/social_share/public/course/cs50x-original.jpg?itok=kR_JV8DW',
        'intro': 'An entry-level course taught by David J. Malan, CS50x teaches students how to think algorithmically and solve problems efficiently.',
        'type': 'website',
        'name': 'cs50',
        'Return': 'free certificate',
        'url':  'https://www.edx.org/course/cs50s-introduction-to-computer-science'
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/6YUQllDI9KrCgiZy8GsMnZ/c38322baa2bfc2d8af1f6ca19ae6e564/maxresdefault.jpg?w=800&h=450&q=50&fm=webp',
        'intro':'This tutorial will teach you modern git and Github',
        'type': 'website',
        'name': 'In Depth Tutorial on Git & Github (DevOps Tools)',
        'url': 'https://www.youtube.com/watch?v=6bjCvZEX52w'
    },
    {
        'id': 0,
        'image': 'https://pr.azureedge.net/img/picresize_logo_registered.png',
        'intro': "visual representaiton of Diffrent Algorithms",
        'type': 'website entrintment',
        'name': 'Visual Algo',
        'url': 'https://visualgo.net/en',
    }
    ,
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/6lslLWTrtJOvT9uKL76BdA/c68fa37469f4052acc66944843ba310a/image.png?w=300&h=168&q=50&fm=webp',
        'intro': "Better understand how far computers have taken us and how far they may carry us.",
        'type': 'free',
        'type': 'playlist',
        'name': 'Crash Course Computer Science',
        'url': 'https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo',
    }
    ,
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/2MdYGTNWLQ4qpBn9lv6Npy/700fed96c05f8149567c70aa871f9bd7/maxresdefault.jpg?w=800&h=450&q=50&fm=webp',
        'intro': "The latest edition of the fantastic, free computer science lectures from Harvard.",
        'type': 'Youtube playlist',
        'name': 'Cs50 2020',
        'url': 'https://youtu.be/Tpl7k8IOT6E',
    }
]
},
    {'api' : [
    {
        'id': 0,
     'image': 'https://i.ytimg.com/vi/yY0ciWj8oco/maxresdefault.jpg',
     'intro': 'A JSON API for pulling headlines and news articles from news sources and blogs across the web',
     'type':'websites','name': 'News API',
     'url': 'https://newsapi.org/https://www.codingblocks.net/'
    },
    {
        'id': 0,
     'image': 'https://devlinduldulao.pro//wp-content/uploads/2017/12/jsonplaceholder-api.png',
     'intro': 'Free to use fake Online REST API for testing and prototyping.',
     'type':'websites','name': 'JSON Placeholder API',
     'url': 'https://jsonplaceholder.typicode.com/'
    },
    {
        'id': 0,
     'image': 'https://cdn.slidesharecdn.com/ss_thumbnails/voicerssapipresentation-140129132037-phpapp01-thumbnail-4.jpg',
     'intro': 'PI for converting text to speech with support for many different languages and voices.',
     'type':'websites','name': 'News APIVoice RSS Text-to-Speech API',
     'url': 'http://www.voicerss.org/api/'
    },
    {
        'id': 0,
     'image': 'https://miro.medium.com/max/3756/1*EEn-tB8M38krdKQuuTR-9Q.png',
     'intro': 'pen-source API for generating random user data',
     'type':'websites','name': 'Random User Generator API',
     'url': 'https://randomuser.me/'
    },
    {
        'id': 0,
     'image': 'https://www.connectioncafe.com/wp-content/uploads/2018/07/API-Design-Skills.png',
     'intro': 'Collection of APIs on a list of issues ranging from health to geocoding',
     'type':'websites','name': 'Useful API’s',
     'url': 'https://github.com/public-apis/public-apis'
    },
]
},
{
    'name': 'motivation',
'start' : [
    {
        
    }
]
},
                  {
    'image': 'https://benjweinberg.files.wordpress.com/2017/08/what-is-an-definite-and-indefinite-articles-hd.png',
    'name': 'Interwiew',
    'start': [
        {
        'id': 0,
        'image': 'https://miro.medium.com/max/5760/1*T9rTWkhfFE47aiBtG5vjXA.jpeg',
        'intro': "A free tool built to provide the complete interview practice you need from Technical to behavioral interviews.",
        'name': 'Pramp',
        'type': 'Website',
        'url': 'https://www.pramp.com/',
        },
        {
        'id': 0,
        'image': 'https://raw.githubusercontent.com/30-seconds/30-seconds-of-interviews/master/promo.jpg',
        'intro': "A collection of common interview questions that will help you prepare for your next interview!",
        'name': '30 seconds of interviews',
        'type': 'Website',
        'url': 'https://30secondsofinterviews.org/',
        },
        {
        'id': 0,
        'image': 'https://beta.techcrunch.com/wp-content/uploads/2017/09/iio_screenshot.jpg',
        'intro': " An excellent, free tool to practice your interviewing skills (technical and soft) anonymously with engineers from established tech companies like Google, AWS, AirBnB, LinkedIn, Lyft, and more!",
        'name': 'Interviewing.io:',
        'type': 'Websites',
        'url': 'https://interviewing.io/',
        },
        {
        'id': 0,
        'image': 'https://img.sur.ly/thumbnails/620x343/g/gainlo.co.png',
        'intro': "A free tool, similar to Interviewing.io, where one can hone their interviewing skills (technical and soft) through mock interviews with engineers from established tech companies - think Google, AirBnB, Amazon, Facebook, Dropbox, etc. - and receive real feedback on how one can improve. Great for those who care more about their privacy than they do their anonymity.",
        'name': 'Gainlo',
        'type': 'Google sheet',
        'url': "http://www.gainlo.co/#!/",
        },
        {
        'id': 0,
        'image': 'https://yangshun.github.io/tech-interview-handbook/img/logo.svg',
        'intro': " Remote pair programming interviewing tool with shared code editor, compiler and video conferencing.",
        'name': 'Adaface',
        'type': 'Google sheet',
        'url': 'https://www/adaface.com/pair-pro',
        },
        {
        'id': 0,
        'image': 'https://yangshun.github.io/tech-interview-handbook/img/logo.svg',
        'intro': "A site for coding challenges and interview prep (including examples of real-world coding challenges/interview questions from various tech companies, including Google, Facebook, and the like)",
        'name': 'CoderByte',
        'type': 'Coding Challenges',
        'url': 'https://www.coderbyte.com/',
        },
        {
        'id': 0,
        'image': 'https://yangshun.github.io/tech-interview-handbook/img/logo.svg',
        'intro': "A place where you can practice coding, prepare for interviews, and get hired.",
        'name': 'HackerRank',
        'type': 'Coding Challenges',
        'url': 'https://www.hackerrank.com/',
        },
        {
        'id': 0,
        'image': 'https://yangshun.github.io/tech-interview-handbook/img/logo.svg',
        'intro': ": Formerly CodeFights, this site has real-world coding questions as well as challenges to keep your skills sharp and help you prepare for interviews.",
        'name': 'CodeSignal',
        'type': 'Coding Challenges',
        'url': 'https://www.codesignal.com/',
        },
        {
        'id': 0,
        'image': 'https://yangshun.github.io/tech-interview-handbook/img/logo.svg',
        'intro': "A place to challenge yourself and hone your coding skills. See if you can find any fellow ZTM students on there and team up!",
        'name': 'Codewars',
        'type': 'Coding Challenges',
        'url': 'https://www.codewars.com/',
        },
        {
        'id': 0,
        'image': 'https://yangshun.github.io/tech-interview-handbook/img/logo.svg',
        'intro': "A complete computer science study plan to become a software engineer.",
        'name': 'Coding Interview University',
        'type': 'Google sheet',
        'url': 'https://github.com/jwasham/coding-interview-university',
        },
    {
        'id': 0,
        'image': 'https://miro.medium.com/max/1909/1*ywYwvB-aydv0Ovx7K-5P3g.jpeg',
        'intro': """A top-notch resource to supplement alongside Andrei’s course, Master The Coding Interview: Data Structures + Algorithms. It features a Google Engineer’s deep-dive into interviewing well amongst a broad array of tech companies (both established and starting up), covering topics such as:

Getting The Interview
Building A Solid Foundation (Big-O, Algorithms, Data Structures)
Tips and Tools to Practice Interviewing Questions
Preparation Process as an Experienced Engineer, New Grad, or Intern
System Design Interviews
Phone Interviews
On-Site Interviews
Non-Technical Questions “Non-Google” Interviews""",
        'name': 'Remote Dev Job Sites',
        'type': 'Google sheet',
        'url': 'http://bit.ly/2NSgGe1',
        },{
        'id': 0,
        'image': 'https://miro.medium.com/max/1909/1*ywYwvB-aydv0Ovx7K-5P3g.jpeg',
        'intro': "Some notes and code associated with a Udemy course titled JavaScript Interview Prep. While the notes themselves may be useful, it is really the process of writing these type of notes that fully prepares one for a technical interview.",
        'name': 'Notes for Coding Interviews',
        'type': 'Artices',
        'url': 'https://pulamusic.github.io/Moon/coding-interviews/',
        },{
        'id': 0,
        'image': 'https://cdn-media-1.freecodecamp.org/images/1*pU1kb1JfF45YbKgZ2zm9dg.png',
        'intro': "Some good, fairly detailed advice on job hunting, networking, interviewing, and negotiation",
        'name': 'How to Break Into the Tech Industry',
        'type': 'Artices',
        'url': 'https://haseebq.com/how-to-break-into-tech-job-hunting-and-interviews/',
        },{
        'id': 0,
        'image': 'https://miro.medium.com/max/1909/1*ywYwvB-aydv0Ovx7K-5P3g.jpeg',
        'intro': "(Artices)How to negotiate a better deal for yourself in the hiring process.",
        'name': 'How to negotiate a better deal for yourself in the hiring process.',
        'type': 'Artices',
        'url': 'https://medium.freecodecamp.org/how-not-to-bomb-your-offer-negotiation-c46bb9bc7dea',
        },
            {
        'id': 0,
        'image': 'https://cdn-media-1.freecodecamp.org/images/1*8csA-fy8rMONaEVeOjVP4A.png',
        'intro': "(Artices)Zhia Chong - a Twitter Software Engineer who possesses a wealth of experience as both an interviewer and interviewee - provides several tips on preparing for programming interviews as well as recommending a solid list of tools and resources (like Cracking The Coding Interview).",
        'name': '5 Things You Need to Know in a Programming Interview',
        'type': 'Artices',
        'url': 'https://medium.freecodecamp.org/the-most-important-things-you-need-to-know-for-a-programming-interview-3429ac2454b',
        },
            
                {
        'id': 0,
        'image': 'https://miro.medium.com/max/1909/1*ywYwvB-aydv0Ovx7K-5P3g.jpeg',
        'intro': "(Artices)A new take on the age-old question: Should you rewrite your application from scratch, or is that “the single worst strategic mistake that any software company can make”? ",
        'name': 'Lessons from 6 software rewrite stories',
        'type': 'Artices',
        'url': 'https://medium.com/@herbcaudill/lessons-from-6-software-rewrite-stories-635e4c8f7c22',
        },
    {
        'id': 0,
        'type': 'Artices',
        'image': 'https://cdn-media-1.freecodecamp.org/images/1*3pyJUEclXtPt8TNONerTUg.jpeg',
        'intro': "(Artices)How to escape tutorial purgatory as a new developer — or at any time in your career.",
        'name': 'For a long time I held off from starting my own side projects because of how much I didn’t know how to do.',
        'url': 'https://www.freecodecamp.org/news/how-to-escape-tutorial-purgatory-as-a-new-developer-or-at-any-time-in-your-career-e3a4b2384a40/',
    },
    {
        'id': 0,
        'type': 'Artices',
        'image': 'https://cdn-media-1.freecodecamp.org/images/1*3pyJUEclXtPt8TNONerTUg.jpeg',
        'intro': "(Artices)How to escape tutorial purgatory as a new developer — or at any time in your career.",
        'name': 'For a long time I held off from starting my own side projects because of how much I didn’t know how to do.',
        'url': 'https://www.freecodecamp.org/news/how-to-escape-tutorial-purgatory-as-a-new-developer-or-at-any-time-in-your-career-e3a4b2384a40/',
    },
    {
        'id': 0,
        'type': 'Artices',
        'image': 'https://cdn-media-1.freecodecamp.org/images/1*3pyJUEclXtPt8TNONerTUg.jpeg',
        'intro': "(Artices)How to escape tutorial purgatory as a new developer — or at any time in your career.",
        'name': 'For a long time I held off from starting my own side projects because of how much I didn’t know how to do.',
        'url': 'https://www.freecodecamp.org/news/how-to-escape-tutorial-purgatory-as-a-new-developer-or-at-any-time-in-your-career-e3a4b2384a40/',
    },
            
      
    
]
},

{
    'image' : 'https://media.geeksforgeeks.org/wp-content/cdn-uploads/20191213191344/Why-Data-Structures-and-Algorithms-Are-Important-to-Learn.png',
    'name': 'DataStructures_Algorithms',
    'start': [
    {
        'id': 0,
        'image': 'https://www.telcoma.in/en/wp-content/uploads/2019/09/Mastering-Data-Structures-Algorithms-using-C-and-C0-.jpg',
        'intro': "Download Free Your Desired AppIntroduction to Algorithms Introduction to course. Why we write Algorithm? Who writes Algorithm? When Algorithms are written? Differences between Algorithms and Programs",
        'type': "Youtube videos",
        'name': 'Abdul Bari: YouTubeChannel for Algorithms',
        'url': 'https://www.youtube.com/watch?v=0IAPZzGSbME&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=2&t=0s',
    },
    {
        'id': 0,
        'image': 'https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190529171221/Learning-Data-Structures-and-Algorithms-is-Important1-1024x424.png',
        'intro': "Hey guys, we have created this channel to provide quality education to students who want to learn, grow and do something beautiful with their life",
        'type': "Youtube videos",
        'name': 'Data Structures and algorithms',
        'url': 'https://www.youtube.com/watch?v=lxja8wBwN0k&list=PLKKfKV1b9e8ps6dD3QA5KFfHdiWj9cB1s',
    },
    {
        'id': 0,
        'image': 'https://miro.medium.com/max/1024/1*9QRFQdpO2f59GsN2KsE9XA.png',
        'intro': "Data Structure & Algorithms course is the most easiest way, that also at free of cost. This playlist has been created by WsCube Tech to help you learn and understand the concepts of Data Structure Algorithm(DSA). All videos cover a wide range of topics and explain each topic with practical examples. You can easily learn about Data Structure Algorithm(DSA), Subscribe the channel to get the latest videos. ",
        'type': "Youtube videos(Hindi)",
        'name': 'Data Structures and algorithms Course',
        'url': 'https://www.youtube.com/playlist?list=PLmGElG-9wxc9Us6IK6Qy-KHlG_F3IS6Q9',
    },
    {
        'id': 0,
        'image': 'https://miro.medium.com/max/1024/1*9QRFQdpO2f59GsN2KsE9XA.pnghttps://i.ytimg.com/vi/CvSOaYi89B4/maxresdefault.jpg',
        'intro': "What are algorithms and why should you care? We'll start with an overview of algorithms and then discuss two games that you could use an algorithm to solve more efficiently - the number guessing game and a route-finding game.",
        'type': "videos + exersise",
        'name': 'Khan Academy',
        'url': 'https://www.khanacademy.org/computing/computer-science/algorithms',
    },
    {
        'id': 0,
        'image': 'https://miro.medium.com/max/1000/0*ZzOeJHpQQk4RhhWW.png',
        'intro': " Pre-requisite for this lesson is good understanding of pointers in C. In this series of lessons, we will study and implement data structures. We will be implementing these data structures in c or c++.  Pre-requisite for this lesson is good understanding of pointers in C. Watch this series on pointers before starting on this series: ",
        'type': "Youtube videos",
        'name': 'Data structures by mycodeschool',
        'url': 'https://www.youtube.com/playlist?list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P',
    },

]
},
]

    
everyydaytools = [
            
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/4tfKlG1Ylr94FeVUQH5Oic/2bfef3e8d5536a47e52e6e5f50c258c8/og-square.png?w=640&h=640&q=50&fm=webp',
        'intro': "An interactive map of popular screen sizes showing the responsive and adaptive device landscape",
        'type':'websites','name': 'Screen Size Map',
        'url': 'https://www.screensizemap.com/',
    }
    ,
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5FX7FgtToDupaRBZuRFW3m/3e822bfe48221fe462ba9205ead4be9b/image.png',
        'intro': "Automatically remove an image background with no clicks and for free in 5 seconds.",
        'type':'websites','name': 'Image Background Remover',
        'url': 'https://www.remove.bg/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/3D1UOB3RrnRLcTtMytmyJa/284a58d52a99d52ded174c17790daeb8/image.png?w=800&h=421&q=50&fm=webp',
        'intro': "Create and share beautiful images of your source code.",
        'type':'websites','name': 'Codeimg.io',
        'url': 'https://codeimg.io/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/2SSyh2voG8mIcUlkpNDDbp/850fa97bd0d109fb16e318edbbfaa7db/image.png',
        'intro': "Free online tools for bulk image processing (resize, crop, compress and more).",
        'type':'websites','name': 'Bulk Image Processing',
        'url': 'https://www.imgbot.ai/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/71B5MfU2Oe5l9BNITmQYYi/ca1fd6bf70dbbf19879648232f4f2497/screenshot.png?w=800&h=450&q=50&fm=webp',
        'intro': "Develop responsive web apps 5x faster. A must-have DevTool for all Front-End developers that will ma",
        'type':'websites','name': 'Responsively',
        'url': 'https://responsively.app/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5UJgTMBsuDqpV1JVgOryvn/59e8e7289d63ba2cd2c6eb884f18014b/image.png?w=304&h=166&q=50&fm=webp',
        'intro': "The most complete resource for the best monospace coding fonts.",
        'type':'websites','name': 'Programming Fonts',
        'url': 'https://app.programmingfonts.org/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/11n7eqjDE3UFlt5v6OkRBT/dd0beaf8e09dc2a61c651833f3ed553f/image.png?w=800&h=416&q=50&fm=webp',
        'intro': "A tool to debug and generate meta tag code for any website.",
        'type':'websites','name': 'Meta Tags',
        'url': 'https://metatags.io/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/4kVxycBS3keteNdBmEDsC8/abbd160757896407cd696c964719dfda/image.png?w=175&h=175&q=50&fm=webp',
        'intro': "Lorem Ipsum... but for photos.",
        'type':'websites','name': 'Lorem Picsum',
        'url': 'https://picsum.photos/',
    },
     {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5iPXVJ2jpDKGyPyfcHhMJ9/36b7d3f8af92ab6703f94b6152e5c547/image.png?w=676&h=676&q=50&fm=webp',
        'intro': "Collection of open APIs (movies, weather, food, news, and more) for development",
        'type':'websites','name': 'Public APIs',
        'url': 'https://public-apis.xyz/',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5b7A0ciaL5LU4wmb2ZYG0v/bb681d4a2c55c2b3c5aedb3479dda7e7/5aecb012-4bda-467c-9782-1ef157aec0d2?w=800&h=450&q=50&fm=webp',
        'intro': "Instantly resize and crop your photos & images for all web and social media formats with one click",
        'type':'websites','name': 'Free Image and Photo Resizer',

        'url': 'https://promo.com/tools/image-resizer/'
    },
    {


        'url': 'https://promo.com/tools/image-resizer/',
    },
    {

        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/1YefYhckdPwmjhjvfUhsI7/c3371fb888864ad70bb0af1b40bf54de/image.png',
        'intro': "Use generative art for your image placeholders.",
        'type':'websites','name': 'Generative Placeholders',
        'url': 'https://generative-placeholders.glitch.me/',
    },
]
   
awesome_websites = [
       {
        'id': 0,
        'image': 'https://freebiesui.com/wp-content/uploads/2020/11/Multipurpose-App-UI-KIt-263x238.jpg',
        'intro': "Are you looking for App Designs, UI Kits or Mockups? Download for free great freebies for Photoshop, Sketch, Principle & XD from FreebiesUI.",
        'name': 'freebiesui',
        'type': "Pattern for use",
        'url': 'https://freebiesui.com/'
    },
    {
        'id': 0,
        'image': 'https://cdn.dribbble.com/users/554451/screenshots/14111195/pattern-collect_4x.png',
        'intro': "A curated gallery of patterns by awesome designers & illustrators",
        'name': 'patterncollect',
        'type': "Pattern for use",
        'url': 'https://patterncollect.com/'
    },
    {
        'id': 0,
        'image': 'https://www.edmsauce.com/wp-content/uploads/2017/11/programming-music.png',
        'intro': "task = (task === undefined) ? 'programming' : task; return 'A series of mixes intended for listening while '+task+' to aid concentration and increase productivity (also compatible with other activities).",
        'name': 'musicforprogramming',
        'type': "Music",
        'url': 'https://www.musicforprogramming.net/'
    },
    {
        'id': 0,
        'image': 'https://jonkuperman.com/static/9d5f8d15762e685534467c67e2cf281f/72e01/joshwcomeau.jpg',
        'intro': 'As I was going through rebuilding my blog, I spent a lot of time looking at other people’s sites trying to get inspiration. Below is a list of my absolute favorite blog designs and my favorite thing about them.',
        'name': 'jonkuperman/best-blog-designs',
        'type': "best-blog-designs",
        'url': 'https://www.joshwcomeau.com/'
    },
        {
            
        
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/3aqr7XDogg9jcGnUglJYOt/05488b640b4307bf3a2e96259bc9bd39/image.png',
        'intro': 'Free resource of 100k high-quality faces, each entirely generated by AI.',
        'name': '100,000 AI-Generated Faces',
        'type': "Ai Photos",
        'url': 'https://generated.photos/'
    
    
    },
  {
        'id': 0,
        'image': 'https://ichef.bbci.co.uk/news/800/cpsprodpb/2E61/production/_110537811_ec96af27-c995-4ed0-b977-9fb4f1d05d3f.jpg',
        'intro': "The Spinner* is a service that enables you to subconsciously influence a specific person, by controlling the content on the websites he or she usually visits. The targeted person gets repetitively exposed to hundreds of items which are placed and disguised as editorial content.",
        'type':'websites','name': 'thespinner',
        'url': 'https://www.thespinner.net/',
    },
    {
        'id': 0,
        'image': 'https://pr.azureedge.net/img/picresize_logo_registered.png',
        'intro': "PicResize.com was created in March 2005 and is the original picture editing tool on the Internet. The service has always remained free to use and has processed more than 150 million pictures since its launch",
        'type':'websites','name': 'pixel resize',
        'url': 'https://picresize.com/en/results#',
    }
    ,
    {
        'id': 0,
        'image': 'https://kk.org/img/bloglogos/KevinKelly1-logo-sketch.gif',
        'intro': "a must read palce to broden your understanding if you are ",
        'type':'websites','name': 'Kevin kelly',
        'url': 'https://kk.org/',
    }
    ,
    {
        'id': 0,
        'image': 'https://twinery.org/homepage/img/logo.svg',
        'intro': "You don't need to write any code to create a simple story with Twine, but you can extend your stories with variables, conditional logic, images, CSS, and JavaScript when you're ready.",
        'sum+up': "where you can write stories",
        'type':'websites','name': 'twine',
        'url': 'https://twinery.org/',
    },
    {

        'id': 0,
        'image': 'https://www.irishnews.com/picturesarchive/irishnews/irishnews/2018/09/21/161005946-89fb1e98-8158-4b08-9bbd-dc01a0736cda.jpg',
        'intro': "Hit the bongos like Bongo Cat!",
        'type':'websites','name': 'Bango cat',
        'url': 'https://bongo.cat/?fbclid=IwAR1xcOLH5dyp3tKne-uVMOAESHQxX3Ep6sBBSh6EdaL6Gzr8aZkgZITFY8E',
    },
    {

        'id': 0,
        'image': 'https://phreesite.com/wp-content/uploads/2018/12/audiobook-Bay-alternatives-.jpg',
        'intro': "Download unabridged audiobook for free or share your audio books, safe, fast and high quality! Safe to get and share audio book here and downloading speed",
        'type':'websites','name': 'AudioBook Bay',
        'url': 'http://audiobookbay.nl/',
    },
    {

        'id': 0,
        'image': 'https://10ideesrecuesenuxdesign.castoretpollux.com/UX-issuesImgMeta.png',
        'intro': "Misconceptions stick. Here are our gems: 10 common misconceptions about design interface our designers often hear about. Can you outsmart the traps?",
        'type':'websites','name': '10ideesrecuesenuxdesign',
        'url': 'https://10ideesrecuesenuxdesign.castoretpollux.com/en/',
    },
      {

        'id': 0,
        'image': 'https://image.winudf.com/v2/image/Y29tLml5dG9yLmVyZXJ6X3NjcmVlbl82XzE1MzU0MDY1NDZfMDIy/screen-6.jpg?fakeurl=1&type=.jpg',
        'intro': "skribbl.io is a free multiplayer drawing and guessing game. One game consists of a few rounds in which every round someone has to draw their chosen word and others have to guess it to gain points! The person with the most points at the end of game will then be crowned as the winner!",
        'type':'websites','name': 'skribbl',
        'url': 'https://skribbl.io/',
    },
    
      {

        'id': 0,
        'image': 'https://10ideesrecuesenuxdesign.castoretpollux.com/UX-issuesImgMeta.png',
        'intro': "Misconceptions stick. Here are our gems: 10 common misconceptions about design interface our designers often hear about. Can you outsmart the traps?",
        'type':'websites','name': '10ideesrecuesenuxdesign',
        'url': 'https://10ideesrecuesenuxdesign.castoretpollux.com/en/',
    },
    
      {

        'id': 0,
        'image': 'https://10ideesrecuesenuxdesign.castoretpollux.com/UX-issuesImgMeta.png',
        'intro': "Misconceptions stick. Here are our gems: 10 common misconceptions about design interface our designers often hear about. Can you outsmart the traps?",
        'type':'websites','name': '10ideesrecuesenuxdesign',
        'url': 'https://10ideesrecuesenuxdesign.castoretpollux.com/en/',
    },
    
      {

        'id': 0,
        'image': 'https://10ideesrecuesenuxdesign.castoretpollux.com/UX-issuesImgMeta.png',
        'intro': "Misconceptions stick. Here are our gems: 10 common misconceptions about design interface our designers often hear about. Can you outsmart the traps?",
        'type':'websites','name': '10ideesrecuesenuxdesign',
        'url': 'https://10ideesrecuesenuxdesign.castoretpollux.com/en/',
    },
    
          {
            
        
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/3aqr7XDogg9jcGnUglJYOt/05488b640b4307bf3a2e96259bc9bd39/image.png',
        'intro': 'Free resource of 100k high-quality faces, each entirely generated by AI.',
        'type':'websites','name': '100,000 AI-Generated Faces',
        'type': "Ai Photos",
        'url': 'https://generated.photos/'
    
    
    },
    {
        'id': 0,
        'image': 'https://ichef.bbci.co.uk/news/800/cpsprodpb/2E61/production/_110537811_ec96af27-c995-4ed0-b977-9fb4f1d05d3f.jpg',
        'intro': "The Spinner* is a service that enables you to subconsciously influence a specific person, by controlling the content on the websites he or she usually visits. The targeted person gets repetitively exposed to hundreds of items which are placed and disguised as editorial content.",
        'type':'websites','name': 'thespinner',
        'url': 'https://www.thespinner.net/',
    },
    {
        'id': 0,
        'image': 'https://pr.azureedge.net/img/picresize_logo_registered.png',
        'intro': "PicResize.com was created in March 2005 and is the original picture editing tool on the Internet. The service has always remained free to use and has processed more than 150 million pictures since its launch",
        'type':'websites','name': 'pixel resize',
        'url': 'https://picresize.com/en/results#',
    }
    ,
    {
        'id': 0,
        'image': 'https://kk.org/img/bloglogos/KevinKelly1-logo-sketch.gif',
        'intro': "a must read palce to broden your understanding if you are ",
        'type':'websites','name': 'Kevin kelly',
        'url': 'https://kk.org/',
    }
    ,
    {
        'id': 0,
        'image': 'https://twinery.org/homepage/img/logo.svg',
        'intro': "You don't need to write any code to create a simple story with Twine, but you can extend your stories with variables, conditional logic, images, CSS, and JavaScript when you're ready.",
        'sum+up': "where you can write stories",
        'type':'websites','name': 'twine',
        'url': 'https://twinery.org/',
    }
    
    
]
game_development = [
    {
        'id': 0,
        'image': 'https://files.hubhopper.com/podcast/12514/real-talk-javascript.jpg',
        'intro': 'A sub-reddit for begginers/intermediate game developers where you can ask by sharing videos/links of specific game events, it will really help you in learning game development.',
        'name': 'How Did They Code It',
        'url': 'https://www.reddit.com/r/howdidtheycodeit/'
    },
    {
        'id': 0,
        'image': 'https://d1p8pldpmo4u0v.cloudfront.net/wp-content/uploads/2016/08/Indie_Game_The_Movie_Artwork_1.jpg',
        'intro': ' A facebook group with 120k+ members who help you if your stuck in your project or for networking and get to know about their stories.',
        'name': 'Indie Game Developers',
        'url': 'https://www.facebook.com/groups/IndieGameDevs/about/'
    },
    {
        'id': 0,
        'image': 'https://www.badykov.com/images/2019-04-06-gamedev.jpg',
        'intro': 'A subreddit with 490k+ members ,where you get to know about game development, programming, design, writing, math, art, jams, postmortems and marketing.',
        'name': 'gamedev:',
        'url': 'https://www.reddit.com/r/gamedev/'
    },
  {
        'id': 0,
        'image': 'https://i.ytimg.com/vi/5LhA4Tk_uvI/maxresdefault.jpg',
        'intro': 'Netwokring documentations which are best to learn how to implement multiplayer game features in your project.',
        'name': 'Mirror Networking',
        'url': 'https://mirror-networking.com/docs/'
    },
    {
        'id': 0,
        'image': 'https://cdn.arstechnica.net/wp-content/uploads/2018/02/ARCore-logo.jpg',
        'intro': 'Documentation to implement AR using Unity.',
        'name': 'ARCore',
        'url': 'https://developers.google.com/ar/develop/unity'
    },
     {
        'id': 0,
        'image': 'https://blogs.unity3d.com/wp-content/uploads/2017/09/ML-blog-header-v6.jpg',
        'intro': 'Tutorials on ML agents.',
        'name': 'ML Agents',
        'url': 'https://www.immersivelimit.com/tutorials/unity-ml-agents-tutorial-list'
    },
    {
        'id': 0,
        'image': 'https://hackernoon.com/drafts/1k3j3zqp.png',
        'intro': '10 Reasons Why You Should Learn How To Develop Video Games',
        'name': 'hackernoon article',
        'url': 'https://hackernoon.com/10-reasons-why-you-should-keep-learning-game-development-hf3l3zmn'
    },
    {
        'id': 1,
        'image': 'https://blogs.unity3d.com/wp-content/uploads/2019/04/Unity-Learn-blog-header_1280x720.jpg',
        'intro': 'Unity Learn provides award-winning free tutorials, sample projects, and full courses for mastering real-time 3D development skills with Unity Learn',
        'type':'websites','name': 'Unity learn',
        'url':  'https://learn.unity.com/'
    },
    {
        'id':2,
        'image': 'https://cdn2.unrealengine.com/Unreal+Engine%2Fonlinelearning-courses%2FNews_UOLDec_fb_image-1200x630-520419d3e9c82ff29459b6844fb50ed0262e715c.jpg',
        'intro': 'Unreal Online Learning is a free learning platform that offers hands-on video courses and guided learning paths.',
        'type':'websites','name': 'unreal engine',
        'url':  'https://www.unrealengine.com/en-US/onlinelearning-courses'
    },
]  
freecourses = [
    
    {   
        'name': "learn computer science in 6 months free",
        'image': 'https://sikshaedunation.in/assets/img/courses/2.jpg',
        
        "start": [
            {
                'id':0,
        'image': 'https://prod-discovery.edx-cdn.org/media/course/image/9e0d9bd0-8557-49bc-a949-4fc7ff7727ac-c1670bfffbc8.small.jpg',
        'intro': 'This is CS50’s introduction to technology for students who don’t (yet!) consider themselves computer persons. ',
        'name': "CS50's Understanding Technology",
        'Return': 'free certificate',
        'type': 'course + Assigments',
        'url':  'https://www.edx.org/course/cs50s-understanding-technology'
            },
            {
                'id':0,
        'image': 'https://online-learning.harvard.edu/sites/default/files/styles/social_share/public/course/cs50x-original.jpg?itok=kR_JV8DW',
        'intro': 'An entry-level course taught by David J. Malan, CS50x teaches students how to think algorithmically and solve problems efficiently.',
        'name': 'cs50',
        'Return': 'free certificate',
        'type': 'course + Assigments',
        'url':  'https://www.edx.org/course/cs50s-introduction-to-computer-science'
            }
            ,
            {
                'id':0,
                'image': 'https://automatetheboringstuff.com/images/cover_beyond_thumb.png',
                'intro': "In Automate the Boring Stuff with Python, you'll learn how to use Python to write programs that do in minutes what would take you hours to do by hand-no prior programming experience required",
                'name': 'Automate the Boring Stuff with Python',
                'Return': 'free certificate',
                'type': 'book',
                'url':  'https://automatetheboringstuff.com/'
            },
            {
                'id':0,
                'image': 'https://thetechxplosion.com/wp-content/uploads/2019/12/images-61009089388099625492..jpg',
                'intro': "Learn the latest and greatest version of the most popular programming language in the world!",
                'name': 'Learn Python 3 pro',
                'Return': 'free certificate',
                'type': 'book',
                'url':  'https://automatetheboringstuff.com/'
            },
            {
                'id':0,
                'image': 'https://courses.csail.mit.edu/6.006/fall11/csaillogosmall.gif',
                'intro': "Introduction to Algorithms By Mit This section provides video lectures, lecture transcripts, and lecture notes for each session of the course.",
                'name': 'Introduction to Algorithms By Mit',
                'Return': 'Base Knowledge',
                'type': 'book + video',
                'url':  'https://courses.csail.mit.edu/6.006/fall11/notes.shtml'
            }
            ,
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/7b3e45ca-d79b-48e3-9b78-4e91f4209e3b-4b6a590c9549.small.jpg',
                'intro': "Learn about data structures that are used in computational thinking – both basic and advanced.",
                'name': 'Data Structures Fundamentals',
                'Return': 'Data Structures',
                'type': 'book + video',
                'url':  'https://www.edx.org/course/data-structures-fundamentals'
            }
            ,
            {
                'id':0,
                'image': 'https://data-flair.training/blogs/wp-content/uploads/sites/2/2018/07/Database-Access-with-Python-3-01-1200x720.jpg',
                'intro': "This course will introduce students to the basics of the Structured Query Language (SQL) as well as basic database design for storing data as part of a multi-step data gathering, analysis, and processing effort.  The course will use SQLite3 as its database",
                'name': 'Using Databases with Python',
                'Return': 'Data Structures',
                'type': 'video + assigment',
                'url':  'https://www.coursera.org/learn/python-databases'
            }
            ,
            {
                'id':0,
                'image': 'https://s3.amazonaws.com/coursera_assets/meta_images/generated/XDP/XDP~COURSE!~computer-networking/XDP~COURSE!~computer-networking.jpeg',
                'intro': "This course is designed to provide a full overview of computer networking. We’ll cover everything from the fundamentals of modern networking technologies and protocols to an overview of the cloud to practical applications and network troubleshooting. ",
                'name': 'The Bits and Bytes of Computer Networking by google',
                'Return': 'computer networking',
                'type': 'video + assigment',
                'url':  'https://www.coursera.org/learn/computer-networking'
            }
            
           
            ,
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/b3c02aea-cbf6-4fc4-a730-0433860e2a35-bb25bbe40de7.small.jpg',
                'intro': "Learn to use powerful, open-source, Python tools, including Pandas, Git and Matplotlib, to manipulate, analyze, and visualize complex datasets.",
                'name': 'Python for Data Science',
                'Return': 'Data science',
                'type': 'video + assigment',
                'url':  'https://www.edx.org/course/python-for-data-science-2'
            }
            ,
            {
                'id':0,
                'image': 'https://miro.medium.com/max/1000/1*k500wvs7Qev35Yd9wOUEvg.jpeg',
                'intro': "This course provides an introduction to computer vision including fundamentals of image formation, camera imaging geometry, feature detection and matching, multiview geometry including stereo, motion estimation and tracking, and classification",
                'name': 'Introduction to Computer Vision',
                'Return': 'Natural Language Processing',
                'type': 'video + assigment',
                'url':  'https://www.udacity.com/course/introduction-to-computer-vision--ud810'
            }
            ,
            {
                'id':0,
                'image': 'https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera-course-photos.s3.amazonaws.com/21/381850484011e6a1703762dd1d87c0/python_datascience_thumbnail_textmining_1x1.png',
                'intro': "This course will introduce the learner to text mining and text manipulation basics. The course begins with an understanding of how text is handled by python, the structure of text both to the machine and to humans, and an overview of the nltk framework for manipulating text. The second week focuses on common manipulation needs, including regular expressions (searching for text), cleaning text, and preparing text for use by machine learning processes. The third week will apply basic natural language processing methods to text, and demonstrate how text classification is accomplished. The final week will explore more advanced methods for detecting the topics in documents and grouping them by similarity (topic modelling). ",
                'name': 'Applied Text Mining in Python',
                'Return': 'Comuter vison to read real world',
                'type': 'video + assigment',
                'url':  'https://www.coursera.org/learn/python-text-mining'
            }
            ,
            {
                'id':0,
                'image': 'https://cdn.velvetech.com/wp-content/uploads/2019/08/software-development-life-cycle.jpg',
                'intro': "In this course,  you will get an overview of  how software teams work? What processes they use?  What are some of the industry standard methodologies? What are pros and cons of each?  You will learn enough to have meaningful conversation around software development processes.",
                'name': 'Software Development Processes and Methodologies',
                'Return': 'Software Engineering Practices',
                'type': 'video + assigment',
                'url':  'https://www.coursera.org/learn/software-processes'
            }
            
        ]
    },
    {
        'name': "learn Machine learning in 6 months free",
        'image': 'https://miro.medium.com/max/2400/1*c_fiB-YgbnMl6nntYGBMHQ.jpeg',
      
        'start':[
            {
                'id':0,
        'image': 'https://img.youtube.com/vi/FX4C-JpTFgY/0.jpg',
        'intro': 'This course parallels the combination of theory and applications in Professor Strang’s textbook Introduction to Linear Algebra. The course picks out four key applications in the book: Graphs and Networks; Systems of Differential Equations; Least Squares and Projections; and Fourier Series and the Fast Fourier Transform.',
        'name': "Linear Algebera",
        'month':'1',
        'Return': 'free',
        'type': 'course + Assigments',
        'url':  'https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/'
            },
            {
                'id':0,
        'image': 'https://i.ytimg.com/vi/WUvTyaaNkzM/hqdefault.jpg',
        'intro': 'The goal here is to make calculus feel like something that you yourself could have discovered.',
        'name': "Essence of calculus",
        'month':'1',
        'Return': 'free',
        'type': 'Youtube course + Assigments',
        'url':  'https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr'
            },
            {
                'id':0,
        'image': 'https://prod-discovery.edx-cdn.org/media/course/image/84251067-b212-4355-a9d3-246d91896b90-41bac59be40f.small.jpg',
        'intro': 'Build foundational knowledge of data science with this introduction to probabilistic models, including random processes and the basic elements of statistical inference -- Part of the MITx MicroMasters program in Statistics and Data Science.',
        'name': "Probability - The Science of Uncertainty and Data",
        'month':'1',
        'Return': 'free',
        'type': 'course + Assigments',
        'url':  'https://www.edx.org/course/probability-the-science-of-uncertainty-and-data'
            },
            {
                'id':0,
        'image': 'https://algs4.cs.princeton.edu/cover.png',
        'intro': 'This course covers the essential information that every serious programmer needs to know about algorithms and data structures, with emphasis on applications and scientific performance analysis of Java implementations. Part I covers elementary data structures, sorting, and searching algorithms. Part II focuses on graph- and string-processing algorithms.',
        'name': "Algorithms, Part I",
        'month':'1',
        'Return': 'free',
        'type': 'course + Assigments',
        'url':  'https://www.coursera.org/learn/algorithms-part1'
            },
            {
                'id':0,
        'image': 'https://i0.wp.com/examinedexistence.com/wp-content/uploads/2013/10/math-equation_chalkboard.jpg',
        'intro': "Welcome to The Math of Intelligence! In this 3 month course, we'll cover the most fundamental math concepts in Machine Learning. In this first lesson, we'll go over a very popular optimization technique called gradient descent to help us predict how many calories a cyclist would burn given just their distance traveled. We'll also follow the story of 2 data scientists as they attempt to find the Higgs-Boson (God particle) via anomaly detection. No collaborations, this is an independent course. ",
        'name': "Math of Intelligence",
        'month':'2',
        'Return': 'free',
        'type': 'course + Assigments',
        'url':  'https://www.youtube.com/watch?v=xRJCOz3AfYY&list=PL2-dafEMk2A7mu0bSksCGMJEmeddU_H4D&ab_channel=SirajRaval'
            },
            {
                'id':0,
        'image': 'https://i.ytimg.com/vi/MotG3XI2qSs/maxresdefault.jpg',
        'intro': "Machine Learning represents a new paradigm in programming, where instead of programming explicit rules in a language such as Java or C++, you build a system which is trained on data to infer the rules itself. But what does ML actually look like? In part one of Machine Learning Zero to Hero, AI Advocate Laurence Moroney (lmoroney@) walks through a basic Hello World example of building an ML model, introducing ideas which we'll apply in later episodes to a more interesting problem: computer vision.",
        'name': "Algorithms, Part I",
        'month':'2',
        'Return': 'free',
        'type': 'course + Assigments',
        'url':  'https://www.youtube.com/watch?v=KNAWp2S3w94&t=4s&ab_channel=TensorFlow'
            },
            {
                'id':0,
        'image': 'https://i.ytimg.com/vi/nLw1RNvfElg/maxresdefault.jpg',
        'intro': 'This course will introduce the learner to the basics of the python programming environment, including fundamental python programming techniques such as lambdas, reading and manipulating csv files, and the numpy library. The course will introduce data manipulation and cleaning techniques using the popular python pandas data science library and introduce the abstraction of the Series and DataFrame as the central data structures for data analysis, along with tutorials on how to use functions such as groupby, merge, and pivot tables effectively. By the end of this course, students will be able to take tabular data, clean it, manipulate it, and run basic inferential statistical analyses. ',
        'name': "Introduction to Data Science in Python",
        'month':'2',
        'Return': 'free',
        'type': 'course + Assigments',
        'url':  'https://www.coursera.org/learn/python-data-analysis'
            },
            {
                
                'id':0,
        'image': 'https://blog.udacity.com/wp-content/uploads/2016/11/AI_ML_SDC-1024x574.png',
        'intro': 'This class will teach you the end-to-end process of investigating data through a machine learning lens. Learn online, with Udacity.',
        'name': "Introduction to Machine Learning Course",
        'month':'2',
        'Return': 'free',
        'type': 'course + Assigments',
        'url':  'https://www.udacity.com/course/intro-to-machine-learning--ud120'
            
            },
            {
                
                'id':0,
        'image': 'https://i.ytimg.com/vi/Af61SygTVFs/maxresdefault.jpg',
        'intro': 'A curated list of practical deep learning and machine learning project ideas',
        'name': "awesome-project-ideas(github)",
        'month':'2',
        'Return': 'free',
        'type': 'course + Assigments',
        'url':  'https://github.com/NirantK/awesome-project-ideas'
            
            },
            {
                
                'id':0,
        'image': 'https://blog.paperspace.com/content/images/2020/09/Fast.ai-4.0-Newsletter-Banner.jpg',
        'intro': "Welcome to Practical Deep Learning for Coders. This web site covers the book and the 2020 version of the course, which are designed to work closely together. If you haven't yet got the book, you can buy it here. It's also freely available as interactive Jupyter Notebooks; read on to learn how to access them..",
        'name': "Practical Deep Learning for Coders",
        'month':'2',
        'Return': 'free',
        'type': 'course + Assigments',
        'url':  'https://course.fast.ai/'
            
            }
        ]
    },
#     {
#         'image':'https://analyticsindiamag.com/wp-content/uploads/2020/03/32-Free-Online-Courses-and-Certificates-You-can-earn-in-2019.jpg',
#         "name": "learning resources",
#         "start": 
#         [
#             {
#                 'id': 2,
# 'image': 'https://www.codecademy.com/webpack/e908164f059c81faded2866ab983e950.png',
# 'intro': 'Bring your apps and games to life with real-time animation. Rive is a powerful design and animation tool, which allows designers and developers to easily',
# 'name': 'rive 2',
# 'url':'https://www.2dimensions.com/',
# 'extra': 'animation',
# 'price': 'free'
#             },
#              {
#                 'id': 2,
# 'image': 'https://www.codecademy.com/webpack/e908164f059c81faded2866ab983e950.png',
# 'intro': 'Bring your apps and games to life with real-time animation. Rive is a powerful design and animation tool, which allows designers and developers to easily',
# 'name': 'rive 2',
# 'url':"mycodeschool’s playlist: https://bit.ly/1NPQ2wQ ,{# %%} MIT course on YouTube: https://bit.ly/1BEh9DL , Stanford courses on Coursera: https://bit.ly/2g8OALL , The Algorithm Design Manual by Skiena (book): https://amzn.to/2KIEYGB , The Google course on Udacity: https://bit.ly/2t7lRLe , Algorithms (book): https://amzn.to/2KG5b8n",
# 'extra': 'animation',
# 'price': 'free'
#             }
#         ]
#     },
    {
        'image':'https://blog.eduonix.com/wp-content/uploads/2017/07/Software-Development-Tools.jpg',
        "name": "programming tools",
        "start": [
            {
        'id': 0,
        'image': 'https://pr.azureedge.net/img/picresize_logo_registered.png',
        'intro': "visual representaiton of Diffrent Algorithms",
        'type':'websites','name': 'Visual Algo',
        'url': 'https://visualgo.net/en',
            }
        ]
    },
    {
        'image': 'https://resources.workable.com/wp-content/uploads/2017/09/employee-handbook-640x230-1.png',
        "name": "handbook and guides",
        "start": [
            {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/7k2ITsrafHNRdWa4PuXhEx/6ff203074bbdb245c79771ec808605bd/web.dev_learn.PNG?w=800&h=387&q=50&fm=webp',
        'intro': "Structured learning paths to discover everything you need to know about building for the modern web.",
        'type':'websites','name': 'Visual Algo',
        'url': 'https://web.dev/learn/',
            },
            {
                
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/2OZOkKLeAMVSC8OiPDCPg0/b200e92264c0f91d670d0456ee4c884e/van-tay-media-TFFn3BYLc5s-unsplash.jpg',
        'intro': "Carefully curated content to help you ace your next technical interview with a focus on algorithms.",
        'type':'websites','name': 'The Tech Interview Handbook',
        'url': 'https://yangshun.github.io/tech-interview-handbook/introduction/',
            
            },
            {
                
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/7tTIAd75XfjyTTpBoicYHn/e790bb58cb4fbdc2928d79701738da68/curriculum-diagram-full.jpg',
        'intro': "This website is full of useful articles about all things and topics related to programming.",
        'type':'websites','name': 'freeCodeCamp Guide',
        'url': 'https://www.freecodecamp.org/news/',
            
            },
             {
                
        'id': 0,
        'image': 'https://frontendmasters.com/books/front-end-handbook/2019/assets/images/FM_2019Cover_final.jpg',
        'intro': "Front-end engineering: how to learn it and what tools are used when practicing it in 2020.",
        'type':'websites','name': 'freeCodeCamp Guide',
        'url': 'https://frontendmasters.com/books/front-end-handbook/2019/',
            
            }
        ]
    }
]
web_Development = [
    # {
    #             'id':0,
    #             'image': 'https://prod-discovery.edx-cdn.org/media/course/image/8f8e5124-1dab-47e6-8fa6-3fbdc0738f0a-762af069070e.small.jpg',
    #             'intro': "This course picks up where CS50 leaves off, diving more deeply intro the design and implementation of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap.",
    #             'name': "CS50's Web Programming with Python and JavaScript",
    #             'Return': 'free certificate',
    #             'type': 'video + assigment',
    #             'url':  'https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript'
    # },
    {
        'intro': "Download the best Free Themes & Templates developed by Creative Tim.",
        'image': 'https://s.tmimgcdn.com/scr/1204x1146/52500/free-responsive-corporate-template-website-template_52524-0-original.jpg',
        "name": "free templates",
        "start": [
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3omokxCIh3RiqdeL9EBVjb/9cb68edffc9099dcd1f108ab7f6fd18f/image.png',
                'intro': "Free themes and responsive templates to create your portfolio or professional website in minutes.",
                'name': "HTML5 and CSS3 Templates",
                'type': 'free templates',
                'url':  'http://www.mashup-template.com/templates.html'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SFAmpexLh9QOxlxfWxbj4/4022c4a394e7f801933960f32cca8c42/image.png',
                'intro': "Download the best Free Themes & Templates developed by Creative Tim.",
                'name': "72+ Free Themes and Templates",
                'type': 'free templates',
                'url':  'https://www.creative-tim.com/templates/free'
            }
        ]
    }
    ,
    {
        'intro': "From the basics to advanced topics with simple, but detailed explanations.",
        'image': 'https://www.simplilearn.com/ice9/free_resources_article_thumb/X_Reasons_to_learn_Javascript.jpg',
        "name": "javascript",
        "start": [
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "A great curriculum for learning JavaScript from newbie to You Don’t Know JS.",
                'name': "A JavaScript Curriculum",
                'type': 'text',
                'url':  'https://medium.freecodecamp.org/a-beginners-javascript-study-plan-27f1d698ea5e'
            },{
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "Short introduction to Node that has some great information.",
                'name': "The Art of Node",
                'type': 'text',
                'url':  'https://github.com/maxogden/art-of-node#the-art-of-node'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "Eloquent JavaScript goes beyond the cut-and-paste scripts of the recipe books and teaches you to write code that’s elegant and effective. You’ll start with the basics of programming, and learn to use variables, control structures, functions, and data structures. Then you’ll dive into the real JavaScript artistry: higher-order functions, closures, and object-oriented programming. Highly recommended.",
                'name': "Eloquent JavaScript",
                'type': 'text',
                'url':  'https://eloquentjavascript.net/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "by Dr. Axel Rauschmeyer: free online books that delve deep into the Javascript language - always up-to-date with new books on the latest Ecmascript features",
                'name': "Exploring JS: JavaScript books for programmers",
                'type': 'text',
                'url':  'http://exploringjs.com/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "by Ben Aston: It is a medium article describing and throwing light upon the History of JavaScript.",
                'name': "A brief history of JavaScript by Ben Aston",
                'type': 'text',
                'url':  'https://medium.com/@benastontweet/lesson-1a-the-history-of-javascript-8c1ce3bffb17'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "Learn JavaScript with an online community, examples, and tons of more advanced JavaScript topics when you are done. Certificate available too. All free.",
                'name': "FreeCodeCamp Beginning JavaScript: ",
                'type': 'text',
                'url':  'https://www.freecodecamp.org/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "Pragmatic, balanced Functional Programming in JavaScript.",
                'name': "Functional Light JS: ",
                'type': 'text',
                'url':  'https://github.com/getify/Functional-Light-JS'
            },  
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "Why reinvent the wheel every time you run into a problem with JavaScript? This cookbook is chock-full of code recipes that address common programming tasks, as well as techniques for building web apps that work in any browser. Just copy and paste the code samples into your project—you’ll get the job done faster and learn more about JavaScript in the process.",
                'name': "JavaScript Cookbook:",
                'type': 'text',
                'url':  'https://www.safaribooksonline.com/library/view/javascript-cookbook/9781449390211/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "An introduction for new programmers.",
                'name': "JavaScript For Cats",
                'type': 'text',
                'url':  'http://jsforcats.com/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "You will learn programming fundamentals and basic object-oriented concepts using the latest JavaScript syntax. The concepts covered in these lessons lay the foundation for using JavaScript in any environment.",
                'name': "JavaScript Fundamentals on Codecademy",
                'type': 'text',
                'url':  'https://www.codecademy.com/learn/introduction-to-javascript'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "A 7 hour long video with detailed explanations to give a strong foundation in JavaScript fundamentals. Taught by Bob Tabor, one of the most effective web development teachers.",
                'name': "JavaScript Fundamentals for Absolute Beginners:",
                'type': 'Youtube playlist',
                'url':  'https://www.youtube.com/watch?v=ei2HLyHwt-k'
            },
        {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "A weekly podcast discussing the superb language JavaScript.",
                'name': "JavaScript Jabber",
                'type': 'text',
                'url':  "https://devchat.tv/js-jabber/"
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "How it’s done now. From the basics to advanced topics with simple with JavaScript, but detailed explanations.",
                'name': "JavaScript.Info",
                'type': 'text',
                'url':  'http://javascript.info/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "This is a very solid foundation to work with, for anyone who might have struggled with the contexts and how arrow functions, local variables, and prototypes fit into the bigger picture. A quick introduction into the deeper ideas in JavaScript.",
                'name': "JavaScript: The Core",
                'type': 'text',
                'url':  "http://dmitrysoshnikov.com/ecmascript/javascript-the-core-2nd-edition"
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': " An online tutorial that received much praise for explaining Node.js in a well-structured way. It is a book that teaches you to write the code for Node.js and not only rely on third-party libraries. Anyone that wants to have a deep grasp of the Node.js framework will benefit from Mixu’s book.",
                'name': "Mixu’s Node Book",
                'type': 'text',
                'url':  'http://book.mixu.net/node/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "The excellent teachers at Watch and Code have released their beginning JavaScript course for free. If you haven’t been able to learn elsewhere, try this tutorial.",
                'name': "Practical JavaScript",
                'type': 'text',
                'url':  'https://watchandcode.com/p/practical-javascript'
            },
            
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "An annual survey of over 20,000 JavaScript developers regarding the major JavaScript libraries, frameworks, languages, and other tools. A useful resource for understanding where the industry is headed and deciding what to learn next.",
                'name': "State of JavaScript",
                'type': 'text',
                'url':  'https://stateofjs.com/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/4RGBWl2tZ0bYIt0GX7XVw1/25f59ffd9052d12bba2a4f562c2ff25f/image.png',
                'intro': "A great site helps you know the event key of the keyboard.",
                'name': "JavaScript Event Keycodes",
                'type': 'free templates',
                'url':  'http://keycode.info/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "A great tool helps you know the specific browsers with “browserslist search query”. You can see the usage in here.",
                'name': "BrowserList ",
                'type': 'free templates',
                'url':  'https://browserl.ist/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "A helpful tool that breaks down your JavaScript code step-by-step. Helpful for identifying errors and solving errors in your code. Run your code in “Live Programming Mode” to visualize all the steps!",
                'name': "Visualize JavaScript",
                'type': 'Tool',
                'url':  'http://www.pythontutor.com/visualize.html#mode=edit'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': " p5.js a JS client-side library for creating graphics and interactive experiences, based on the core principles of Processing. It has add-on libraries that make it easy to interact with other HTML5 objects, including text, input, video, webcam and sound.",
                'name': "p5.js",
                'type': 'Tool',
                'url':  'https://p5js.org/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "An excellent breakdown of linting’s purpose and history while also giving a thorough analysis of some of the most common linting style-guides (Google, AirBnb, Common) as to what they do differently, what is similar and some of their best use-cases according to the project one is undertaking. A fantastic guide for those who are stuck choosing between which linting style-guide they should use.",
                'name': "Linting ES2015+ — ESLint with StyleGuides: Google, AirBnB, Common",
                'type': 'Tool',
                'url':  'https://medium.com/@uistephen/style-guides-for-linting-ecmascript-2015-eslint-common-google-airbnb-6c25fd3dff0'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "The same tool for objects.",
                'name': "Javascript Object Explorer",
                'type': 'Tool',
                'url':  'https://sdras.github.io/object-explorer/'
            },
            
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "Find the array method you need for your JavaScript array without digging through the docs. A useful resource that can make using arrays easier.",
                'name': "JavaScript Array Explorer",
                'type': 'Tool',
                'url':  'https://sdras.github.io/array-explorer/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "A closure is a function that has access to its outer function scope even after the return of the outer function (For better understanding head inside the blog).",
                'name': "A simple guide to help you understand closures in JavaScript: ",
                'type': 'Advanced Javascript Articles',
                'url':  'https://medium.com/@prashantramnyc/javascript-closures-simplified-d0d23fa06ba4'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "Async/await functions, a new addition with ES2017 (ES8), help us even more in allowing us to write completely synchronous-looking code while performing asynchronous tasks behind the scenes",
                'name': "Exploring Async/Await Functions in JavaScript",
                'type': 'Advanced Javascript Articles',
                'url':  'https://alligator.io/js/async-functions'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "Learn JavaScript ES6 concepts with this short, interactive course at Scrimba. This includes interactive screencasts so you can learn along with the teacher. This is a pretty unique way of instruction",
                'name': "JavaScript ES6: Scrimba:",
                'type': 'Websites',
                'url':  'https://scrimba.com/learn/introtoes6'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "A short interactive website which has exercises for introducing new programmers to the primary concepts in JavaScript.",
                'name': "JavaScript for Complete Beginners - Interactive Tutorial",
                'type': 'Websites',
                'url':  'https://www.learn-js.org/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "javascript exercises for beginners",
                'name': "a smarter way to learn",
                'type': 'Websites',
                'url':  'http://www.asmarterwaytolearn.com/js/index-of-exercises.html'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "This page is a collection of the best articles, videos and presentations related to JavaScript.",
                'name': "Superhero.js",
                'type': 'Websites',
                'url':  'http://superherojs.com/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "A comprehensive video course from beginner to mastery with real world projects.",
                'name': "The Complete JavaScript Course 2020: Build Real Projects!",
                'type': 'Websites',
                'url':  'https://www.udemy.com/course/the-complete-javascript-course/learn/lecture/10788532?start=0#overview'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "JS Tips is a collection of useful daily JavaScript tips that will allow you to improve your code writing.",
                'name': "JS Tips - A JavaScript tip per day!",
                'type': 'Websites',
                'url':  'https://www.jstips.co/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "From the basics to advanced topics with simple, but detailed explanations.",
                'name': "The Modern JavaScript Tutorial",
                'type': 'Websites',
                'url':  'http://javascript.info/'
            },
        ]
    },
    {
        'intro': "From the basics to advanced topics with simple, but detailed explanations.",
                'image': 'https://www.bypeople.com/wp-content/uploads/2019/01/css-animation-101-featured.jpg',
                'type':'websites','name': 'css animation"',
                "start": [
                    {
                        'image': 'https://www.best4webdesign.com/wp-content/uploads/2015/03/css3-animation.jpg',
                        'intro': "AniCollection is the easiest way to find, use and share animations. We are putting together awesome animations from many libraries and many people.",
                        'url': "http://anicollection.github.io/#/",
                        'type':'websites','name': "anicollection"
                    },
                    {
                        'image': 'https://i.ytimg.com/vi/CBQGl6zokMs/maxresdefault.jpg',
                        'intro': "Animate.css is a library of ready-to-use, cross-browser animations for use in your web projects. Great for emphasis, home pages, sliders, and attention-guiding hints.",
                        'url': "https://daneden.github.io/animate.css/",
                        'type':'websites','name': "animate.css"
                    },
                    {
                        'image': 'https://i.ytimg.com/vi/qMTiK0BV5Z0/maxresdefault.jpg',
                        'intro': "ANIMISTA IS A PLACE WHERE YOU CAN PLAY WITH A COLLECTION OF PRE-MADE CSS ANIMATIONS, TWEAK THEM AND GET ONLY THOSE YOU WILL ACTUALLY USE.",
                        'url': "http://animista.net/",
                        'type':'websites','name': "animista.net   "
                    },
                    {
                        'image': 'https://frontntweaks.com/wp-content/uploads/2019/12/thumbnail650.jpg',
                        'intro': "Anime.js is a small, lightweight JavaScript library with a simple and small powerful API. It works with the DOM element, CSS, and JavaScript object.",
                        'url': "http://animejs.com/",
                        'type':'websites','name': "animejs.com"
                    },
                    {
                        'image': 'https://vuejsexamples.com/content/images/2018/01/epic-spinners-1.png',
                        'intro': "We’re working on Vuestic UI component library, which lets you easily customize components to your own design.Get early access and receive support from the core team! 😎",
                        'url': "https://epic-spinners.epicmax.co/#/",
                        'type':'websites','name': "Css only. Easy to use. VueJS integration."
                    },
                    {
                        'image': 'https://cdn.dribbble.com/users/580/screenshots/2362765/spinkit.gif',
                        'intro': "Simple loading spinners animated with CSS. See demo. SpinKit only uses (transform and opacity) CSS animations to create smooth and easily customizable animations.",
                        'url': "http://tobiasahlin.com/spinkit/",
                        'type':'websites','name': "loading spinners animated with CSS."
                    },
                ]
            },
    {
        'intro': "A tool to generate soft-UI CSS code for neumorphic card designs.",
        'image': 'https://pixelmechanics.com.sg/wp-content/uploads/2019/04/css.jpg',
        "name": "css",
        "start": [
            
    {
        'id':0,
        'image': 'https://miro.medium.com/max/1200/1*d7_iZtG8vNH0OJrAc1SwIQ.png',
        'intro': "A tool to generate soft-UI CSS code for neumorphic card designs.",
        'name': "Neumorphism",
        'type': 'CSS_Tools',
        'url':  'https://neumorphism.io/'
    },
    {
        'id':0,
        'image': 'https://www.lapa.ninja/assets/blog/doodad.jpg',
        'intro': "Highly customizable pattern generator. Can create unique patterns and has a nice shuffle function also.",
        'name': "Doodad Pattern Generator",
        'type': 'CSS_Tools',
        'url':  'https://doodad.dev/pattern-generator/'
    },
    {
        'id':0,
        'image': 'https://responsively.app/assets/img/screenshot.png',
        'intro': "This app helps you to get preview all target screens in a single window side-by-side.",
        'name': "Responsively App",
        'type': 'CSS_Tools',
        'url':  'https://responsively.app/'
    },
    {
        'id':0,
        'image': 'https://www.noupe.com/wp-content/uploads/2013/01/easing.png',
        'intro': "This page helps you choose the right easing function for your CSS animations.",
        'name': "Easings.net",
        'type': 'CSS_Tools',
        'url':  'https://easings.net/'
    },
    {
        'id':0,
        'image': 'https://michael.chtoen.com/image/ultimate-css-gradient-generator.jpg',
        'intro': "A CSS gradient generator, that allows multiple colorstops and different kinds of gradients.",
        'name': "Ultimate CSS Gradient Generator",
        'type': 'CSS_Tools',
        'url':  'http://www.colorzilla.com/gradient-editor/'
    },
    {
        'id':0,
        'image': 'https://miro.medium.com/max/3000/0*Y03deVPEIa7AypAo.png',
        'intro': "Create fast loading, highly readable, and 100% responsive interfaces with as little css as possible.",
        'name': "Tachyons",
        'type': 'CSS_Tools',
        'url':  'https://tachyons.io/'
    },
    {
        'id':0,
        'image': 'https://9elements.github.io/fancy-border-radius/fancy-border-radius.png',
        'intro': "Generator that helps you create organic looking shapes with border radius.",
        'name': "Fancy Border Radius",
        'type': 'CSS_Tools',
        'url':  'https://9elements.github.io/fancy-border-radius/'
    },
    {
        'id':0,
        'image': 'https://s3.amazonaws.com/coursetro/posts/content_images/3-1520178989301.png',
        'intro': "A great tool for creating bezier curve animations in CSS without having to guess at the code.",
        'name': "cubic-bezier.com",
        'type': 'CSS_Tools',
        'url':  'http://cubic-bezier.com/#.17,.67,.83,.67'
    },
    {
        'id':0,
        'image': 'https://www.bypeople.com/wp-content/uploads/2014/02/tooltip-arrows-generator.jpg',
        'intro': "Create and export CSS code for a custom box with an arrow extending out from the side.",
        'name': "CSS Arrow Please",
        'type': 'CSS_Tools',
        'url':  'http://www.cssarrowplease.com/'
    },
    {
        'id':0,
        'image': 'https://www.bram.us/wordpress/wp-content/uploads/2017/06/css-clip-path-maker.png',
        'intro': "A tool that helps you create shapes and generate its equivalent CSS code.",
        'name': "Clippy – CSS clip-path maker",
        'type': 'CSS_Tools',
        'url':  'https://bennettfeely.com/clippy/'
    },
    {
        'id':0,
        'image': 'https://ph-files.imgix.net/1572cc90-fdc9-4df8-8373-70697695f597.png',
        'intro': "Generate beautiful blob shapes for web and flutter apps.",
        'name': "Blobs",
        'type': 'CSS_Tools',
        'url':  'https://blobs.app/'
    },
    {
        'id':0,
        'image': 'https://user-images.githubusercontent.com/33191954/78983001-0a0ef880-7b43-11ea-904f-42a572d93c53.png',
        'intro': "Really cool collection of loading spinners with React.js",
        'name': "React Spinners",
        'type': 'CSS_Tools',
        'url':  'https://github.com/davidhu2000/react-spinners'
    },
    {
        'id':0,
        'image': 'https://regexr.com/assets/card.png',
        'intro': "An online tool to learn, build, & test Regular Expressions (RegEx / RegExp).",
        'name': "RegExr",
        'type': 'CSS_Tools',
        'url':  'https://regexr.com/'
    },
    {
        'id':0,
        'image': 'https://d2qlddhczasafd.cloudfront.net/img/marketing/product-16x9@2x.png',
        'intro': "A server for your static websites and HTML forms.",
        'name': "Pageclip",
        'type': 'CSS_Tools',
        'url':  'https://pageclip.co/'
    },
     {
        'id':0,
        'image': 'https://extendsclass.com/image/me.png',
        'intro': "An online toolbox for developers: Playgrounds (XPath, Regex, JavaScript and SQL), HTTP clients (SOAP, REST), formatters, converters and encoders.",
        'name': "ExtendsClass",
        'type': 'CSS_Tools',
        'url':  'https://extendsclass.com/'
    },
    {
        'id':0,
        'image': 'https://miro.medium.com/max/1200/1*57WtFAIwhYej3eIAFzM71A.jpeg',
        'intro': "A curated repository of Tools for FrontEnd developers..",
        'name': "FrontEnd Tools",
        'type': 'CSS_Tools',
        'url':  'http://frontendtools.com/'
    },
    {
        'id':0,
        'image': 'https://sweetalert2.github.io/images/sweetalert2-social.png',
        'intro': "Some really nice looking alerts that you can use.",
        'name': "SweetAlert2:",
        'type': 'CSS_Tools',
        'url':  'https://sweetalert2.github.io/?utm_content=buffer5396d&utm_medium=social&utm_source=facebook.com&utm_campaign=buffer'
    },
    {
        'id':0,
        'image': 'https://sweetalert2.github.io/images/sweetalert2-social.png',
        'intro': "Some really nice looking alerts that you can use.",
        'name': "SweetAlert2:",
        'type': 'CSS_Tools',
        'url':  'https://sweetalert2.github.io/?utm_content=buffer5396d&utm_medium=social&utm_source=facebook.com&utm_campaign=buffer'
    },

            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/30kC4o240eHFh0fE6n1PYH/09dbf4e8ca8e19f761a9d754ba4fa50f/image.png?w=800&h=486&q=50&fm=webp',
                'intro': "Classic tower defense game but using CSS to position your towers.",
                'name': "Flexbox Defense",
                'type': 'css Games',
                'url':  'http://www.flexboxdefense.com/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/4tUaHeYUpOP2f5Tv5dTX0F/2ecfc593dae0f7f439501c01e321285b/image.png',
                'intro': "Broswer game to practice identifying HTML selectors for use in CSS stylesheets.",
                'name': "CSS Diner",
                'type': 'css Games',
                'url':  'https://css-diner.netlify.app/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/72nixprDE0M0fwwMkQZbYN/7ce860cb66c6f22eedd8913108d70d2a/image.png',
                'intro': "A browser game where you write CSS code to help you learn CSS grid layout.",
                'name': "Grid Garden",
                'type': 'css Games',
                'url':  'https://cssgridgarden.com/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/58rc7QCmF0ifFvXxUhsi0l/35dcdd264a17a62f830b9584b8d866e1/image.png',
                'intro': "A game for learning CSS flexbox.",
                'name': "Flexbox Froggy",
                'type': 'css Games',
                'url':  'https://flexboxfroggy.com/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/6ngsa311Hwbe2HeUFcVfEf/22a19b83a3f063cdefc9909cb5c4a9c0/banner.png?w=800&h=421&q=50&fm=webp',
                'intro': "CSS code-golfing! Use CSS to replicate targets with smallest possible code",
                'name': "CSSBattle",
                'type': 'css Games',
                'url':  'https://cssbattle.dev/'
            },
            
        ]
    },
    {'intro': "online code editors",
        'image': 'https://pixelmechanics.com.sg/wp-content/uploads/2019/04/css.jpg',
        "name": "online code editor",
    'start' : [
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
                    },
                    {
'intro': "Chrome extention for better workflow",
        'image': 'https://pixelmechanics.com.sg/wp-content/uploads/2019/04/css.jpg',
        "name": "Chrome extentions",
                    'start': [
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
                    },
  
    
                    
]
web_designer = [
 {

     
 }
]
android_cources = [
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/8f8e5124-1dab-47e6-8fa6-3fbdc0738f0a-762af069070e.small.jpg',
                'intro': "This course picks up where CS50 leaves off, diving more deeply intro the design and implementation of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap.",
                'name': "CS50's Web Programming with Python and JavaScript",
                'Return': 'free certificate',
                'type': 'video + assigment',
                'url':  'https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript'
            },
            {
                
                'id':0,
                'image': 'https://developer.android.com/images/kotlin/learn/hero.svg',
                'intro': "Whether you're interested in getting started with Kotlin or are looking to grow your expertise, Google's Kotlin for Android training courses can help you advance your skills.",
                'name': "Learn Kotlin for Android",
                'Return': 'free certificate',
                'type': 'video + text + assigment',
                'url':  'https://developer.android.com/kotlin/campaign/learn'
            
            },
            {
                
                'id':0,
                'image': 'https://developer.android.com/courses/images/android-for-developers.svg',
                'intro': "Whether you're interested in getting started with Kotlin or are looking to grow your expertise, Google's Kotlin for Android training courses can help you advance your skills.",
                'name': " All Android courses provided by google",
                'Return': 'free certificate',
                'type': 'video + text + assigment',
                'url':  'https://developer.android.com/courses'
            
            },
            {
                'id':0,
                'image': 'https://1onjea25cyhx3uvxgs4vu325-wpengine.netdna-ssl.com/wp-content/uploads/2016/06/Develop-for-Android-Chalkboard.jpg',
                'intro': "This course is designed for students who are new to programming, and want to learn how to build Android apps. You don’t need any programming experience to take this course. If you’ve been using a smartphone to surf the web and chat with friends, then you’re our perfect target student!",
                'name': "Android Basics: User Interface",
                'Return': 'certificate',
                'type': 'video +  assigment',
                'url':  'https://www.udacity.com/course/android-basics-nanodegree-by-google--nd803'
            },
            {
                'id':0,
                'image': 'https://s3-us-west-1.amazonaws.com/udacity-content/partner/logo-color-google-1c8cf8f.svg',
                'intro': "Learn to architect and develop Android apps in the Kotlin programming language using industry-proven tools and libraries. With these techniques you'll create apps in less time, writing less code, and with fewer errors.",
                'name': "Developing Android Apps with Kotlin",
                'Return': 'certificate',
                'type': 'video +  assigment',
                'url':  'https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012'
            },
            {
                'id':0,
                'image': 'https://s3-us-west-1.amazonaws.com/udacity-content/partner/logo-color-google-1c8cf8f.svg',
                'intro': "Learn to architect and develop Android apps in the Kotlin programming language using industry-proven tools and libraries. With these techniques you'll create apps in less time, writing less code, and with fewer errors.",
                'name': "Developing Android Apps with Kotlin",
                'Return': 'certificate',
                'type': 'video +  assigment',
                'url':  'https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012'
            }
            
        ]
android_resources = [
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
android_learning = [
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/8f8e5124-1dab-47e6-8fa6-3fbdc0738f0a-762af069070e.small.jpg',
                'intro': "This course picks up where CS50 leaves off, diving more deeply intro the design and implementation of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap.",
                'name': "CS50's Web Programming with Python and JavaScript",
                'Return': 'free certificate',
                'type': 'video + assigment',
                'url':  'https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript'
            },
            {
                'id':0,
                'image': 'https://abhiandroid-8fb4.kxcdn.com/ui/wp-content/uploads/2018/05/Abhi-Android.png',
                'intro': "website for understanding of andtroid topics",
                'name': "Abhi android",
                'type': 'text',
                'url':  'https://abhiandroid.com/'
            }
            ,
            {
                'id':0,
                'image': 'https://abhiandroid-8fb4.kxcdn.com/ui/wp-content/uploads/2018/05/Abhi-Android.png',
                'intro': "website for understanding of andtroid topics",
                'name': "codelabs for android by google",
                'type': 'text',
                'url':  'https://codelabs.developers.google.com/codelabs'
            },
            {
                'id':0,
                'image': 'https://camo.githubusercontent.com/be3b1262c26ff23b3480c07c4b13ca1d01355a73/68747470733a2f2f692e696d6775722e636f6d2f586778576679462e706e67',
                'intro': "We have Android guides for everyone whether you are a beginner, intermediate or expert. Want to learn how to use the ActionBar or the ins and outs of fragments? We got that. Want to learn about automated unit testing or how to build flexible user interfaces for multiple devices? ",
                'name': "an android guide (github code_path)",
                'type': 'text',
                'url':  'https://github.com/codepath/android_guides/wiki'
            }
        ]
android_development = [
    {
        "cources": [
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/8f8e5124-1dab-47e6-8fa6-3fbdc0738f0a-762af069070e.small.jpg',
                'intro': "This course picks up where CS50 leaves off, diving more deeply intro the design and implementation of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap.",
                'name': "CS50's Web Programming with Python and JavaScript",
                'Return': 'free certificate',
                'type': 'video + assigment',
                'url':  'https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript'
            },
            {
                
                'id':0,
                'image': 'https://developer.android.com/images/kotlin/learn/hero.svg',
                'intro': "Whether you're interested in getting started with Kotlin or are looking to grow your expertise, Google's Kotlin for Android training courses can help you advance your skills.",
                'name': "Learn Kotlin for Android",
                'Return': 'free certificate',
                'type': 'video + text + assigment',
                'url':  'https://developer.android.com/kotlin/campaign/learn'
            
            },
            {
                
                'id':0,
                'image': 'https://developer.android.com/courses/images/android-for-developers.svg',
                'intro': "Whether you're interested in getting started with Kotlin or are looking to grow your expertise, Google's Kotlin for Android training courses can help you advance your skills.",
                'name': " All Android courses provided by google",
                'Return': 'free certificate',
                'type': 'video + text + assigment',
                'url':  'https://developer.android.com/courses'
            
            },
            {
                'id':0,
                'image': 'https://1onjea25cyhx3uvxgs4vu325-wpengine.netdna-ssl.com/wp-content/uploads/2016/06/Develop-for-Android-Chalkboard.jpg',
                'intro': "This course is designed for students who are new to programming, and want to learn how to build Android apps. You don’t need any programming experience to take this course. If you’ve been using a smartphone to surf the web and chat with friends, then you’re our perfect target student!",
                'name': "Android Basics: User Interface",
                'Return': 'certificate',
                'type': 'video +  assigment',
                'url':  'https://www.udacity.com/course/android-basics-nanodegree-by-google--nd803'
            },
            {
                'id':0,
                'image': 'https://s3-us-west-1.amazonaws.com/udacity-content/partner/logo-color-google-1c8cf8f.svg',
                'intro': "Learn to architect and develop Android apps in the Kotlin programming language using industry-proven tools and libraries. With these techniques you'll create apps in less time, writing less code, and with fewer errors.",
                'name': "Developing Android Apps with Kotlin",
                'Return': 'certificate',
                'type': 'video +  assigment',
                'url':  'https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012'
            },
            {
                'id':0,
                'image': 'https://s3-us-west-1.amazonaws.com/udacity-content/partner/logo-color-google-1c8cf8f.svg',
                'intro': "Learn to architect and develop Android apps in the Kotlin programming language using industry-proven tools and libraries. With these techniques you'll create apps in less time, writing less code, and with fewer errors.",
                'name': "Developing Android Apps with Kotlin",
                'Return': 'certificate',
                'type': 'video +  assigment',
                'url':  'https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012'
            }
            
        ]
                
    },
    {
        "resources": [
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
        'name': 'giphy.com',
        'url': 'https://giphy.com/',
        'extra': 'Giphy',
        'price': 'free',
        'type': "gifs",
    },
        ]
    },
    {
        "learning": [
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/8f8e5124-1dab-47e6-8fa6-3fbdc0738f0a-762af069070e.small.jpg',
                'intro': "This course picks up where CS50 leaves off, diving more deeply intro the design and implementation of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap.",
                'name': "CS50's Web Programming with Python and JavaScript",
                'Return': 'free certificate',
                'type': 'video + assigment',
                'url':  'https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript'
            },
            {
                'id':0,
                'image': 'https://abhiandroid-8fb4.kxcdn.com/ui/wp-content/uploads/2018/05/Abhi-Android.png',
                'intro': "website for understanding of andtroid topics",
                'name': "Abhi android",
                'type': 'text',
                'url':  'https://abhiandroid.com/'
            }
            ,
            {
                'id':0,
                'image': 'https://abhiandroid-8fb4.kxcdn.com/ui/wp-content/uploads/2018/05/Abhi-Android.png',
                'intro': "website for understanding of andtroid topics",
                'name': "codelabs for android by google",
                'type': 'text',
                'url':  'https://codelabs.developers.google.com/codelabs'
            },
            {
                'id':0,
                'image': 'https://camo.githubusercontent.com/be3b1262c26ff23b3480c07c4b13ca1d01355a73/68747470733a2f2f692e696d6775722e636f6d2f586778576679462e706e67',
                'intro': "We have Android guides for everyone whether you are a beginner, intermediate or expert. Want to learn how to use the ActionBar or the ins and outs of fragments? We got that. Want to learn about automated unit testing or how to build flexible user interfaces for multiple devices? ",
                'name': "an android guide (github code_path)",
                'type': 'text',
                'url':  'https://github.com/codepath/android_guides/wiki'
            }
        ]
    }

]
Machine_learning_main = [
    {
        "Month" : 1,
        "Type" : "Maths",
        "start": [
            {
                'id':0,
                'image': 'https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/18-06s10.jpg',
                'intro': "This is a basic subject on matrix theory and linear algebra. Emphasis is given to topics that will be useful in other disciplines, including systems of equations, vector spaces, determinants, eigenvalues, similarity, and positive definite matrices.",
                'name': "Introduction to Linear Algebra.",
                'Return': 'Base knowledge',
                'type': 'video + youtube',
                'url':  'https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/'
            },
            {
                'id':0,
                'image': 'https://i.ytimg.com/vi/WUvTyaaNkzM/maxresdefault.jpg',
                'intro': "The goal here is to make calculus feel like something that you yourself could have discovered.",
                'name': "Essence of linear calculus",
                'Return': 'Base knowledge',
                'type': 'video + youtube',
                'url':  'https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr'
            },
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/84251067-b212-4355-a9d3-246d91896b90-41bac59be40f.small.jpg',
                'intro': "Build foundational knowledge of data science with this introduction to probabilistic models, including random processes and the basic elements of statistical inference -- Part of the MITx MicroMasters program in Statistics and Data Science",
                'name': "Probability - The Science of Uncertainty and Datassence of linear algebra",
                'Return': 'knowledge',
                'type': 'video + assigments',
                'url':  'https://www.edx.org/course/introduction-probability-science-mitx-6-041x-2'
            },
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/8e285de1-0242-4e94-8041-84231363caf4-e1a05f019d47.small.jpg',
                'intro': "Learn about the core principles of computer science: algorithmic thinking and computational problem solving.",
                'name': "Algorithm Design and Analysis",
                'Return': 'Base knowledge',
                'type': 'video + assigment',
                'url':  'https://www.edx.org/course/algorithm-design-analysis-pennx-sd3x'
            },
            


        ]
    },
    {
        "Month" : 2,
        "Type" : "datascience , intellegence , teserflow",
        "start": [
            {
                'id':0,
                'image': 'https://i.ytimg.com/vi/kjBOesZCoqc/maxresdefault.jpg',
                'intro': "A geometric understanding of matrices, determinants, eigen-stuffs and more.",
                'name': "Essence of linear algebra",
                'Return': 'Base knowledge',
                'type': 'video + youtube',
                'url':  'https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab'
            },
        ]
    },
    {
        "Month" : 3,
        "Type" : "Machinelearning",
        "start": [
            {
                'id':0,
                'image': 'https://blog.udacity.com/wp-content/uploads/2015/11/MLND-blog-post-1024x536.png',
                'intro': "This class will teach you the end-to-end process of investigating data through a machine learning lens. Learn online, with Udacity.",
                'name': "Introduction to Machine Learning Course",
                'Return': 'intermidiate knowledge',
                'type': 'video + assigments',
                'url':  'https://www.udacity.com/course/intro-to-machine-learning--ud120'
            },
            {
                'id':0,
                'image': 'https://blog.udacity.com/wp-content/uploads/2015/11/MLND-blog-post-1024x536.png',
                'intro': "A curated list of practical deep learning and machine learning project ideas",
                'name': "Awesome Deep Learning Project Ideas",
                'Return': 'intermidiate knowledge',
                'type': 'practice',
                'url':  'https://github.com/NirantK/awesome-project-ideas'
            }
        ]
    },
    {
        "Month" : 3,
        "Type" : "Deep learning",
        "start": [
            {
                'id':0,
                'image': 'https://i.ytimg.com/vi/kjBOesZCoqc/maxresdefault.jpg',
                'intro': "A geometric understanding of matrices, determinants, eigen-stuffs and more.",
                'name': "Essence of linear algebra",
                'Return': 'Base knowledge',
                'type': 'video + youtube',
                'url':  'https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab'
            },
        ]
    }

]

user_interface = [
    {
'id': 1,
'image':'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5c5957de3e262c46a81b4611_Artboard%2BCopy-p-1600.png',
'intro': 'Slick mockup movies and images for promo videos, presentations, portfolios, app store images.Showcasing like the big boys is no longer just for the big boys.',
'name': 'Rotato',
'url':'https://www.rotato.xyz/',
'type': 'mockups',
'price': 'half free'
    },
    {
'id': 2,
'image': 'https://miro.medium.com/max/1600/1*oxxU6j6GXYODNT2is-KU6Q.gif',
'intro': 'Bring your apps and games to life with real-time animation. Rive is a powerful design and animation tool, which allows designers and developers to easily',
'name': 'rive 2',
'url':'https://www.2dimensions.com/',
'type': 'animation',
'price': 'free'
    },
    {
        'id': 3,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5bf6e0c690b6c76a53804bdc_answers_calculator.png',
'intro': 'Understand how users are really experiencing your site without drowning in numbers Traditional web analytics tools help you analyze traffic data. But numbers alone can’t tell you what users really do on your site — Hotjar will.',
'name': 'hotjar',
'url':'https://www.hotjar.com/?utm_expid=.EinRyQaiRjGYjFEJFTUl4Q.0&utm_referrer=',
'type': 'analytics',
'price': 'paid'
    },
    {
        'id': 4,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5be9b020d015a1f9ec9a5442_banner-2.png',
'intro': 'Are you working with design files? Start saving time today.In all plans you can present, comment, create screen flows, and inspect Sketch, Adobe XD, Photoshop, Illustrator, & Figma files - using our web, macOS, Windows, & Linux app',
'name': 'Avocode',
'url':'https://avocode.com/hand-off-and-inspect',
'type': 'UI/UX designing',
'price': 'paid'
    },
    {
        'id': 5,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5bc453b95a68ee5fe21bc6b4_Screen%20Shot%202018-10-15%20at%2010.45.18%20AM.png',
'intro': 'Are you working with design files? Start saving time today.In all plans you can present, comment, create screen flows, and inspect Sketch, Adobe XD, Photoshop, Illustrator, & Figma files - using our web, macOS, Windows, & Linux app',
'name': 'micro',
'url':'https://realtimeboard.com/',
'type': 'team collaboration for brainstroming + video call',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5ba39a9e805bfa74a4b08ddf_1_F19-hrmAQppP33zh1G2jgQ-p-1600.png',
'intro': 'To empower the work of design teams by facilitating a creative synergy through effortless collaboration.',
'name': 'plant',
'url':'https://plantapp.io/#about',
'type': 'team collaboration for brainstroming + video call',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b866b1515ad26e6cea79353_2017-character_personas.jpg',
'intro': 'Generate professional, customizable buyer persona documents with the help of this quick and intuitive generator.',
'name': 'Make my persona',
'url': 'https://www.hubspot.com/make-my-persona',
'type': 'personal portfolio',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b769ac79183f17ee9fe0942_by%20Norde.png',
'intro': 'Vaadin comes with a big set of web components that are fine-tuned for UX, performance, and accessibility.',
'name': 'vaadin',
'url':'https://vaadin.com/',
'type': 'web apps => java',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b583ac6fc79dd91ac4f68af_30134265966479.5b075bbf1b0a7.jpg',
'intro': 'Discover how real users interact with your prototype: define missions, collect actionable insights and analyze how your design performed, with 0 lines of code.',
'name': 'maze',
'url':'https://maze.design/',
'type': 'ui/ux testing + analytics for prototypes',
'price': 'free 1 month trial'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b3c86048d4e3381013434c0_color-tool-v2-4x3.gif',
'intro': 'The Material Theme Editor helps you make your own branded symbol library and apply global style changes to color, shape, and typography.',
'name': 'gallery',
'url':'https://gallery.io/apps',
'type': 'matrial theme editor',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5afb0c4a5d83d9375a8d19d0_social_tout.png',
'intro': "By choosing a set of 50 colors, you'll train a neural network powered algorithm to generate colors you like and block ones you don’t, right in your browser.",
'name': 'khroma',
'url':'http://khroma.co/',
'type': 'Design with colors you love. Khroma uses AI to learn which colors you like and creates limitless palettes for you to discover, search, and save.',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5ac3825ee45951aaec5936b0_homepage-bg-669c8ea95a9ede671933dffb254f493a23de2d7a039f90bfbbac9ecd09f78225.svg',
'intro': 'Share your ideas visually. Lightning fast.',
'name': 'gallery',
'url':'https://whimsical.co/',
'type': 'brainstrming workspace',
'price': 'create 4 free boards '
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5a5dc7eb3e2b760001e215f4_Illustration%20by%20Iza%20Dudzik.jpg',
'intro': 'Piece hi-fi interactions together, build sensor-aided prototypes and share your amazing creations in a matter of minutes.',
'name': 'protopie',
'url':'https://www.protopie.io/',
'type': 'prototyping tool',
'price': 'free for students'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5a312b470672a700015a499c_brics.gif',
'intro': 'Blocs Website Builder Fast, easy to use and powerful visual web design software, that lets you create responsive websites without writing code.',
'name': 'blocs',
'url':'https://blocsapp.com/',
'type': 'websitebuilder',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9cb80a71c7d00019122e2_lottie.png',
'intro': 'Lottie is an iOS, Android, and React Native library that renders After Effects animations in real time, allowing apps to use animations as easily as they use static images.',
'name': 'lottie',
'url':'https://lottiefiles.com/getting-started#',
'type': 'animation maker',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9c715775aae00019a177c_monotype-library-subscription_lead-image-p-1600.jpeg',
'intro': 'With more than 2,200 font families all in one location, you can easily find the perfect typeface for your project. Whether it’s for your own, a client’s or your company’s design, having complete access to a broad selection of high-quality, premium type is a must.',
'name': 'monotype library',
'url':'https://blocsapp.com/',
'type': 'fonts',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e8a73a90983b000144f01e_webflow.png',
'intro': 'The modern way to build for the web Webflow empowers designers to build professional, custom websites in a completely visual canvas. View dashboard',

'name': 'webflows',
'url':'https://webflow.com/',
'type': 'websitebuilder',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e215007032510001bb636f_home-screenshot.png',
'intro': "Online app that enables designers to customize their own typeface in a few clicks.",
'name': 'prototypo',
'url':'https://www.prototypo.io/',
'type': 'fonts',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e218ae3f6bfa0001113de7_invision-logo.jpg',
'intro': "The world's leading prototyping, collaboration & workflow platform",
'name': 'invision',
'url':'https://www.invisionapp.com/',
'type': 'prototyping + devlopment fro m design',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Adobe_XD_CC_icon.svg/1200px-Adobe_XD_CC_icon.svg.png',
'intro': "Share your story with designs that look and feel like the real thing. Wireframe, animate, prototype, collaborate and more — it’s all right here, all in one place.",
'name': 'Adobe xd',
'url':'https://www.adobe.com/in/products/xd.html',
'type': 'ui/ux designing',
'price': 'free'
    },
    {
        "learning": [
            {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5be9af00cbd406ee1caaff15_expert-advice-unfurl.png',
'intro': "Build your design system like the pros",
'name': 'ui/ux',
'url':'https://www.invisionapp.com/design-system-manager/expert-advice',
'extra': 'ui/ux designing',
'price': 'free',
'type': 'learning+video'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b311fa7cbd2eb17d660c209_ui-guide-Designing-search-for%20mobile-apps-p-1600.jpeg',
'intro': "Explore the various ways to implement search and the purpose behind each",
'name': 'ui/ux',
'url':'https://medium.muz.li/designing-search-for-mobile-apps-ab2593e9e413',
'extra': 'ui/ux designing',
'price': 'free',
'type': 'learning+text'
    }
    ,
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5ac380fbf1502e199b611d42_squarepegroundhole_final4.png',
'intro': "I have always believed that Psychology and Design comprise User Experience.",
'name': 'ui/ux',
'url':'https://uxdesign.cc/psychology-design-4-gestalt-principles-to-use-as-your-next-design-solution-fcdec423a6bf',
'extra': 'ui/ux designing',
'price': 'free',
'type': 'learning+text'
    }
    ,
    {
        'id': 6,
'image': 'https://miro.medium.com/max/700/1*3M9hkYLvrJ5xTR2_ZM0FAg.gif',
'intro': "7 Basic Rules for Button Design",
'name': 'ui',
'url':'https://uxplanet.org/7-basic-rules-for-button-design-63dcdf5676b4',
'extra': 'ui/ux designing',
'price': 'free',
'type': 'learning+text'
    }
    ,
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5a68617439ab7c00014d1d3a_170623_dropbox-ecosystem_v01.jpg',
'intro': "Laws of UX is a collection of the maxims and princples that designers can consider when building user interfaces.",
'name': 'ui',
'url':'https://lawsofux.com/',
'extra': 'ui/ux designing',
'price': 'free',
'type': 'learning+text'
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9c297e87a4d000109e13d_1-t2L7WZC7hpZFexm47qzQSA-p-1600.jpeg',
        'intro': 'Collection of articles, videos, and resources made by designers at Facebook.',
        'name': 'facebook design',
        'url': 'http://facebook.design/',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "learning",
    },
        ],
        "resource" : [
            
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
        'intro': 'Mix-&-match illustrations of people with a design library',
        'name': 'Hummans',
        'url': 'https://www.humaaans.com/?ref=producthunt',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5bf6e3d14ae3421f52814444_download.jpg',
        'intro': 'Mobbin is a hand-picked collection of the latest mobile design patterns from apps that reflect the best in design. Get inspiration from over 150 iOS apps and 8,000 patterns (screenshots from iPhone X) available on the platform. Sign up to save your favorite patterns.',
        'name': 'mobbin',
        'url': 'https://mobbin.design/',
        'extra': 'ios design pattrens',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59fc7d4b605d4b0001f003e9_marriot_copy.jpg',
        'intro': 'Take responsive screenshots with the click of button',
        'name': 'Responsive screenshorts',
        'url': 'https://responsive-screenshots.com/',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "Resource",
    },
    
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5c05205a90375ebb9d52fad7_Image-p-1600.jpeg',
        'intro': 'Mix-&-match illustrations of people with a design library',
        'name': 'Hummans',
        'url': 'https://www.humaaans.com/?ref=producthunt',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9bea6e87a4d000109dbd1_jakub-dziubak-394720-(1).jpg',
        'intro': 'Beautiful high quality free images and photos you can download and use for any project. No attribution required.',
        'name': 'unsplash',
        'url': 'https://unsplash.com/',
        'extra': 'Photos',
        'price': 'free',
        'type': "Resource",
    },
    
    {
        'id': 0,
        'image': 'https://www.logo-designer.co/wp-content/uploads/2013/09/iStock-logo-design-identity-getty-images-Build.jpg',
        'intro': 'free photos',
        'name': 'istock',
        'url': 'https://www.istockphoto.com/collaboration/boards/L9m43WDlbUO8O94wqUFIIA',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://cdn.joypixels.com/sections/coverphotos/6.0%20Release%20FINAL%20FINAL-02-min.png',
        'intro': 'New for 2020! JoyPixels 6.0 includes 3,342 originally crafted icon designs and is 100% Unicode 13 compatible. We offer the largest selection of files ranging from png, svg, iconjar, sprites, and fonts.',
        'name': 'PIXELS',
        'url': 'https://www.joypixels.com/',
        'extra': 'Emoji',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://static-cdn.pixlr.com/images/pixlr-header-logo.png',
        'intro': 'Pixlr, the World’s Favorite #1 Online Photo Editor lets you edit photos right in your browser for Free. Experience next level, intuitive photo editing with AI-powered tools for quick yet professional edits',
        'name': 'PIXLR',
        'url': 'https://www.joypixels.com/',
        'extra': 'Emoji',
        'price': 'free',
        'type': "Resource",
    },

            
        
        ],
        "inspiration" : [
            {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5bf6e3d14ae3421f52814444_download.jpg',
        'intro': 'Mobbin is a hand-picked collection of the latest mobile design patterns from apps that reflect the best in design. Get inspiration from over 150 iOS apps and 8,000 patterns (screenshots from iPhone X) available on the platform. Sign up to save your favorite patterns.',
        'name': 'mobbin',
        'url': 'https://mobbin.design/',
        'extra': 'ios design pattrens',
        'price': 'free',
        'type': "ios + inspiration",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9c90cc3e5160001ed80f0_fb.png',
        'intro': 'The best design inspiration - expertly curated for you. Muzli is a new-tab Chrome extension that instantly delivers relevant design stories and inspiration. Learn more',
        'name': 'Muzil',
        'url': 'https://muz.li/',
        'extra': 'inspiration',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9c297e87a4d000109e13d_1-t2L7WZC7hpZFexm47qzQSA-p-1600.jpeg',
        'intro': 'Collection of articles, videos, and resources made by designers at Facebook.',
        'name': 'facebook design',
        'url': 'http://facebook.design/',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "inspiration",
    },
    {
        'id': 0,
        'image': 'https://s3.amazonaws.com/www-inside-design/uploads/2015/06/Dribbble-InVision-feature.jpg',
        'intro': 'Dribbble is where designers gain inspiration, feedback, community, and jobs and is your best resource to discover and connect with designers worldwide.',
        'name': 'Dribble',
        'url': 'https://dribbble.com/',
        'extra': 'Ui/Ux',
        'price': 'free',
        'type': "inspiration",
    },
    {
        'id': 0,
        'image': 'https://i.pinimg.com/280x280_RS/e9/f7/e1/e9f7e101e3b7484d53b2b4d5a6004740.jpg',
        'intro': 'Behance is a social media platform owned by Adobe which claims "to showcase and discover creative work"',
        'name': 'Behance',
        'url': 'https://www.behance.net/',
        'extra': 'Ui / ux / animation / design 2d / 3d',
        'price': 'free',
        'type': "inspiration",
    },
    {
        'id': 0,
        'image': 'https://cdn-images-1.medium.com/max/1200/1*A0FnBy5FBoVQC02SZXLXPg.png',
        'intro': 'One-stop resource for everything related to user experience"',
        'name': 'uxplanet',
        'url': 'https://uxplanet.org/',
        'extra': 'ux / animation / design 2d / 3d',
        'price': 'free',
        'type': "inspiration",
    }
        ]
    }

    




]

Stock = [
    {
        'image':'https://web3canvas.com/wp-content/uploads/2017/09/free-stock-photography-websites.jpg',
        'type':'websites',
        'name': 'Stock Images',
        'start': 
        [
            {     
                'id': 0,
                'image': 'https://www.pexels.com/assets/pexels-stock-photos-6c3d5eb0cbed47e1bdf44ff85ebd9cd4669f50b895b3c6e76a23a4fd43852099.jpg',
                'intro': 'Free stock photos shared by talented creators',
                'type': 'website',
                'name': 'Pexels',
                'url': 'https://www.pexels.com/',
            },
            {     
                'id': 0,
                'image': 'https://colorlib.com/wp/wp-content/uploads/sites/2/free-stock-photo-websites.jpg',
                'intro': 'The internet’s source of freely usable images',
                'type': 'website',
                'name': 'Unsplash',
                'url': 'https://unsplash.com/',
            },
            {     
                'id': 0,
                'image': 'https://www.bettertechtips.com/wp-content/uploads/2018/01/pixabay.jpg',
                'intro': 'Over 1.7 million+ high-quality stock images and videos',
                'type': 'website',
                'name': 'Pixabay',
                'url': 'https://pixabay.com/',
            },
            {     
                'id': 0,
                'image': 'https://themetix.com/images/wpts-sss/magdeleine.co.jpg',
                'intro': 'Gallery & free high-resolution photo everyday',
                'type': 'website',
                'name': 'Magdeleine',
                'url': 'https://magdeleine.co/',
            },
            {     
                'id': 0,
                'image': 'https://www.inpressionedit.com/wp-content/uploads/2017/08/stock-photo-site-picspree.png',
                'intro': 'Royalty free images, stock photos, illustrations, and vectors',
                'type': 'website',
                'name': 'Picspree',
                'url': 'https://picspree.com/en',
            },
            {     
                'id': 0,
                'image': 'https://cdn.shopifycloud.com/stock_photos/assets/global/burst-share-df978141accd818331ea8b59ac61c9f52dd7a1d26c96db143e3a2593298b00da.jpg',
                'intro': 'Free stock photos collections',
                'type': 'website',
                'name': 'Burst',
                'url': 'https://burst.shopify.com/',
            },
            {     
                'id': 0,
                'image': 'https://www.empowersuite.com/hubfs/gratisography.jpg',
                'intro': 'Free collection of free high-resolution pictures',
                'type': 'website',
                'name': 'Gratisography',
                'url': 'https://gratisography.com/',
            },
            {     
                'id': 0,
                'image': 'https://pic.accessify.com/thumbnails/777x423/l/lifeofpix.com.png',
                'intro': 'Free high-resolution photography',
                'type': 'website',
                'name': 'Life of Pix',
                'url': 'https://www.lifeofpix.com/',
            },
            {     
                'id': 0,
                'image': 'https://i.pinimg.com/600x315/85/88/51/8588519d9423738bb741334c6d0f7629.jpg',
                'intro': 'Hundreds of high quality photos added weekly',
                'type': 'website',
                'name': 'Stock Snap',
                'url': 'https://stocksnap.io/',
            },
            {     
                'id': 0,
                'image': 'https://hayataki-masaharu.jp/wp-content/uploads/2015/12/Morguefile.com-free-stock-photos.png',
                'intro': 'Over 350,000 free stock photos for commercial use',
                'type': 'website',
                'name': 'Morguefile',
                'url': 'https://morguefile.com/',
            },
            {     
                'id': 0,
                'image': 'https://kaboompics.com/uploads/assets/howitworks_1_m.jpg',
                'intro': 'Stock photography and color palettes. Good for product images',
                'type': 'website',
                'name': 'Kaboom Pics',
                'url': 'https://kaboompics.com/',
            },
            {     
                'id': 0,
                'image': 'https://picjumbo.com/wp-content/uploads/picjumbo-promo-image-1.jpg',
                'intro': 'Good collections of different types of photos',
                'type': 'website',
                'name': 'Pic Jumbo',
                'url': 'https://picjumbo.com/',
            },
            {     
                'id': 0,
                'image': 'https://mail.publicdomainpictures.net/static/images/velka/index.jpg',
                'intro': 'Public domain images of all types',
                'type': 'website',
                'name': 'Public Domain Pictures',
                'url': 'https://www.publicdomainpictures.net/en/',
            },
            {     
                'id': 0,
                'image': 'https://img.sur.ly/thumbnails/620x343/f/finda.photo.png',
                'intro': 'Searches multiple stock photo websites',
                'type': 'website',
                'name': 'Find a Photo',
                'url': 'https://www.chamberofcommerce.org/findaphoto/',
            },
            {     
                'id': 0,
                'image': 'https://www.stockvault.net/templates/default/images/logo_square.png',
                'intro': 'Categorized stock photos',
                'type': 'website',
                'name': 'StockVault',
                'url': 'https://www.stockvault.net/',
            },
            {     
                'id': 0,
                'image': 'https://placeholder.com/wp-content/uploads/2019/06/stock-images.png',
                'intro': 'A free image placeholder service for the web. You can specify image size and format',
                'type': 'website',
                'name': 'Placeholder',
                'url': 'https://placeholder.com/',
            },
            {     
                'id': 0,
                'image': 'https://avospy.com/screenshot/http-realisticshots-com.jpg',
                'intro': 'Free high-resolution stock photos',
                'type': 'website',
                'name': 'Realistic Shots',
                'url': 'https://realisticshots.com/',
            },
            {     
                'id': 0,
                'image': 'https://i0.wp.com/www.colourmyincome.com/wp-content/uploads/2019/01/negativespace.jpg',
                'intro': 'High-Resolution Free Stock Photos',
                'type': 'website',
                'name': 'Negative Space',
                'url': 'https://negativespace.co/',
            },
            {     
                'id': 0,
                'image': 'https://pixelixe.com/blog/images/10/skitterphoto.png',
                'intro': 'Free high-resolution photography',
                'type': 'website',
                'name': 'SkitterPhoto',
                'url': 'https://skitterphoto.com/',
            },
            {     
                'id': 0,
                'image': 'https://growthjunkie.com/wp-content/uploads/2018/03/picography1.png',
                'intro': 'Gorgeous, High-Resolution, Free Photos',
                'type': 'website',
                'name': 'PicoGraphy',
                'url': 'https://picography.co/',
            },
            {     
                'id': 0,
                'image': 'https://jasper.monster/sharex/firefox_2020-08-14_21-35-07.png',
                'intro': 'Stunningly amazing free photos',
                'type': 'website',
                'name': 'Wunder Stock',
                'url': 'https://wunderstock.com/',
            },
            {     
                'id': 0,
                'image': 'https://comstrat310.files.wordpress.com/2019/06/pxhere-logo.png',
                'intro': 'Free Images & Free stock photos - PxHere',
                'type': 'website',
                'name': 'PxHere',
                'url': 'https://pxhere.com/',
            },
            {     
                'id': 0,
                'image': 'https://kontactr.com/website/screenshots/piqsels.com-tablet-479a5854dc664295fef3a083a5ba0f96.png',
                'intro': 'Royalty Free Stock Photos',
                'type': 'website',
                'name': 'Piqsels',
                'url': 'https://www.piqsels.com/',
            },
            {     
                'id': 0,
                'image': 'https://i.ytimg.com/vi/GU3ikLKGg1E/maxresdefault.jpg',
                'intro': 'Food photo stock',
                'type': 'website',
                'name': 'FoodiesFeed',
                'url': 'https://www.foodiesfeed.com/',
            },
            {     
                'id': 0,
                'image': 'https://nappy.co/public/img/meta_header.jpg',
                'intro': 'A website offering Beautiful, high-res photos of black and brown people.',
                'type': 'website',
                'name': 'Nappy',
                'url': 'https://www.nappy.co/',
            },
            {     
                'id': 0,
                'image': 'https://miro.medium.com/max/1200/1*pnwbjNtF1SYieRMqVh-NCg.png',
                'intro': 'Unique AI Generated model photos',
                'type': 'website',
                'name': 'Generated Photos',
                'url': 'https://generated.photos/',
            },
            {     
                'id': 0,
                'image': 'https://d3t64pp0gm1u4c.cloudfront.net/build/reshot-og-7c70b5cdf7819975bd2941609b5320f6907f13a435ae36e3f3c2e55c087a4074.png',
                'intro': 'Uniquely free photos. Handpicked, non-stocky images.',
                'type': 'website',
                'name': 'Reshot',
                'url': 'https://www.reshot.com/',
            },
            {     
                'id': 0,
                'image': 'https://www.dioceseofnorwich.org/app/uploads/2019/10/banco-imagenes-free-images-600x330.jpg',
                'intro': 'Find and download free stock photos - all free for personal and commercial use',
                'type': 'website',
                'name': 'Free Images',
                'url': 'https://www.freeimages.com/',
            },
            {     
                'id': 0,
                'image': 'https://www.golem.de/1904/140933-194481-194479_rc.jpg',
                'intro': 'An easy to use API to get beautiful placeholder images. Size and other parameters can be specified.',
                'type': 'website',
                'name': 'Lorem Picsum',
                'url': 'https://picsum.photos/',
            },
            {     
                'id': 0,
                'image': 'https://crastina.se/wp-content/uploads/2020/02/scienceimage.csiro_-300x260.png',
                'intro': 'An image library specializing in science and nature images',
                'type': 'website',
                'name': 'Science Image',
                'url': 'https://www.scienceimage.csiro.au/',
            },
            {     
                'id': 0,
                'image': 'https://slideplayer.com/slide/13548828/82/images/1/Integration+and+Application+Network.jpg',
                'intro': 'Free images to provide scientists, resource managers, government agencies, community groups and graphics professionals with a resource for enhancing science communication.',
                'type': 'website',
                'name': 'Integration & Application Network',
                'url': 'https://ian.umces.edu/imagelibrary/',
            },
            {     
                'id': 0,
                'image': 'https://img.pagecloud.com/DOReoyLJdLUTsF2p6Eci5wSLm7Y=/1000x0/filters:no_upscale()/web/best-stock-images-stocksnap-i69d8.jpg',
                'intro': 'Free nature images',
                'type': 'website',
                'name': 'Saxifraga',
                'url': 'http://www.freenatureimages.eu/',
            },
            {     
                'id': 0,
                'image':'https://cdn.business2community.com/wp-content/uploads/2013/01/creativecommons.jpg',
                'intro': 'Search for free images to reuse.',
                'type':'website',
                'name': 'Creative Commons',
                'url': 'https://search.creativecommons.org/',
            },
            
            
        ]
    },
    {
    'image': 'https://superdevresources.com/wp-content/uploads/2015/05/free-stock-videos-e1524206162551-1280x720.jpg',
    'type':'websites',
    'name': 'Stock Videos',
    'start' :
        [
            {
                'id': 0,
                'image': 'https://trickeza.com/wp-content/uploads/2020/06/Annotation-2020-06-04-013052-1024x485.jpg',
                'intro': "Largest library of free to use videos, donated by the community",
                'type':'website',
                'name': 'Pexels',
                'url': 'https://www.pexels.com/videos',
            },
            {
                'id': 0,
                'image': 'https://i2.wp.com/digonair.com/wp-content/uploads/2018/02/pixabay-1.jpg',
                'intro': "Large library of free to use videos, donated by the community similar to Pexels",
                'type':'website',
                'name': 'Pixabay',
                'url': 'https://pixabay.com/videos/',
            },
            {
                'id': 0,
                'image': 'https://www.noupe.com/wp-content/uploads/2016/09/coverr-landing.jpg',
                'intro': "Beautiful free stock video footage",
                'type':'website',
                'name': 'Coverr.co',
                'url': 'https://coverr.co/',
            },
            {
                'id': 0,
                'image': 'https://i.ytimg.com/vi/-2cMtE0FOnM/hqdefault.jpg',
                'intro': "Free HD stock footage & 4K videos",
                'type':'website',
                'name': 'Videezy',
                'url': 'https://www.videezy.com/',
            },
            {
                'id': 0,
                'image': 'https://assets.mixkit.co/static/OG-meta/video.jpg',
                'intro': "Stock video clips & music",
                'type':'website',
                'name': 'Mix Kit',
                'url': 'https://mixkit.co/',
            },
            {
                'id': 0,
                'image': 'https://techwiser.com/wp-content/uploads/2018/09/Screen-Shot-2018-09-26-at-4.45.10-PM.jpg',
                'intro': "Free video clips and loops",
                'type':'website',
                'name': 'Life of Vids',
                'url': 'https://www.lifeofvids.com/',
            },
            {
                'id': 0,
                'image': 'https://www.videvo.net/wp-content/uploads/2012/05/Videvo-Banner-1.jpg',
                'intro': "Free and premium stock videos",
                'type':'website',
                'name': 'Videvo',
                'url': 'https://www.videvo.net/stock-video-footage/',
            },
            {
                'id': 0,
                'image': 'https://s3-us-west-2.amazonaws.com/steemhunt/production/steemhunt/2020-07-26/bd61d56f-Screenshot%20(779).png',
                'intro': "Free To Use Cinema graphs Created With VIMAGE App",
                'type':'website',
                'name': 'Loopvidz',
                'url': 'http://stock.loopvidz.com/',
            },
            {
                'id': 0,
                'image': 'https://img.dropmark.com/N-tmM3a02xTpQ97J0W7ds1nFb3k=/fit-in/600x600/top/filters:dpr(2):quality(30):frames(0):square()/web/aHR0cHM6Ly93d3cuc3BsaXRzaGlyZS5jb20v.jpg',
                'intro': "Beautiful & exclusive free stock videos & photos",
                'type':'website',
                'name': 'Splitshire',
                'url': 'https://www.splitshire.com/',
            },
        ]
    },

    {
    'image': 'https://www.m2social.ph/wp-content/uploads/2019/07/6-free-stock-music.jpg',
    'type':'websites',
    'name': 'Stock Music and Sound Effects',
    'start' :
        [
            {
                'id': 0,
                'image': 'https://i.pinimg.com/564x/21/71/07/21710785c8dec8923c61205648cc1384.jpg',
                'intro': "Royalty free stock music for YouTube videos, podcasts, etc",
                'type':'website',
                'name': 'Free Stock Music',
                'url': 'https://www.free-stock-music.com/',
            },
            {
                'id': 0,
                'image': 'https://www.videvo.net/wp-content/uploads/2016/09/Screen-Shot-2016-09-25-at-22.25.48.png',
                'intro': "Download Royalty Free Music for free and use it in your project",
                'type':'website',
                'name': 'Bensound',
                'url': 'https://www.bensound.com/',
            },
            {
                'id': 0,
                'image': 'https://assets.mixkit.co/static/OG-meta/music.jpg',
                'intro': "Free music for your projects",
                'type':'website',
                'name': 'Mixkit',
                'url': 'https://mixkit.co/free-stock-music/',
            },
            {
                'id': 0,
                'image': 'https://cdn.shopify.com/s/files/1/0993/3800/files/freesound_grande.jpg',
                'intro': "Free stock music and sounds",
                'type':'website',
                'name': 'Freesound',
                'url': 'https://freesound.org/',
            },
            {
                'id': 0,
                'image': 'https://i.ytimg.com/vi/6CgRJ1Q1BrA/maxresdefault.jpg',
                'intro': "Collaborative database of creative-commons licensed sound for musicians and sound lovers",
                'type':'website',
                'name': 'Free Music Archive',
                'url': 'https://freemusicarchive.org/',
            },
            {
                'id': 0,
                'image': 'https://upload.wikimedia.org/wikipedia/commons/f/fe/Home_page_screen_capture_of_Musopen.org.png',
                'intro': "An online copyright free classical music library",
                'type':'website',
                'name': 'Musopen',
                'url': 'https://musopen.org/music/',
            },
            {
                'id': 0,
                'image': 'https://cdn.webrazzi.com/uploads/2020/03/unminus-802_hd.png',
                'intro': "Free Premium Music for Your Projects 🎁 Royalty Free. Cleared for YouTube",
                'type':'website',
                'name': 'Unminus',
                'url': 'https://www.unminus.com/',
            },
            
        ]
    },
    
    {
    'image': 'https://www.m2social.ph/wp-content/uploads/2019/07/6-free-stock-music.jpg',
    'type':'websites',
    'name': 'Fonts',
    'start' :
        [
            {
                'id': 0,
                'image': 'https://i1.wp.com/css-tricks.com/wp-content/uploads/2018/06/google-fonts.png',
                'intro': "Library of around 1000 free licensed font families",
                'type':'website',
                'name': 'Google Fonts',
                'url': 'https://fonts.google.com/',
            },
            {
                'id': 0,
                'image': 'https://i2.wp.com/thetechhacker.com/wp-content/uploads/2019/12/dafont.com-Review-Best-site-to-download-thousands-of-free-fonts.jpg',
                'intro': "Archive of freely downloadable fonts",
                'type':'website',
                'name': 'DaFont',
                'url': 'https://www.dafont.com/',
            },
            {
                'id': 0,
                'image': 'https://new000000.com/wp-content/uploads/2018/01/useandmodify.png',
                'intro': "Personal selection of beautiful, classy, punk, professional, incomplete, weird typefaces",
                'type':'website',
                'name': 'Use & Modify',
                'url': 'https://usemodify.com/',
            },
            {
                'id': 0,
                'image': 'https://img.sur.ly/thumbnails/620x343/1/1001freefonts.com.png',
                'intro': "I think the name speaks for itself 😏",
                'type':'website',
                'name': '1001 free fonts',
                'url': 'https://www.1001freefonts.com/',
            },
            {
                'id': 0,
                'image': 'https://www.fontsquirrel.com/presentation/theme_site/images/matcherator/matcherator_logo.png',
                'intro': "Font Squirrel scours the internet for high quality, legitimately free fonts",
                'type':'website',
                'name': 'Font Squirrel',
                'url': 'https://www.fontsquirrel.com/',
            },
            {
                'id': 0,
                'image': 'https://www.fontfabric.com/blog/wp-content/uploads/2019/09/blog_fontfabric_past_and_future_cover.png',
                'intro': "A digital type foundry crafting retail fonts and custom typography for various brands",
                'type':'website',
                'name': 'Font Fabric',
                'url': 'https://www.fontfabric.com/free-fonts/',
            },
            {
                'id': 0,
                'image': 'https://pic.accessify.com/thumbnails/777x423/t/tiff.herokuapp.com.png',
                'intro': "A type diff tool that visually contrasts the differences between two fonts",
                'type':'website',
                'name': 'Tiff',
                'url': 'https://tiff.herokuapp.com/',
            },
            {
                'id': 0,
                'image': 'https://i.pinimg.com/originals/06/3a/75/063a75536166799a50f19b5593e90a6c.png',
                'intro': "Learn about typography practices",
                'type':'website',
                'name': 'TypeKit Practice',
                'url': 'https://practice.typekit.com/',
            },
            {
                'id': 0,
                'image': 'https://assets.hongkiat.com/uploads/font-pairing-tool-fontjoy/01-pairing-made-simple.jpg',
                'intro': "Generate font pairing in one click",
                'type':'website',
                'name': 'Fontjoy',
                'url': 'https://fontjoy.com/',
            },
            {
                'id': 0,
                'image': 'https://s3-us-west-2.amazonaws.com/steemhunt/production/steemhunt/2019-04-10/c08ba046-calc.png',
                'intro': "Golden Ratio Typography Calculator",
                'type':'website',
                'name': 'Golden Ratio',
                'url': 'https://grtcalculator.com/',
            },
            {
                'id': 0,
                'image': 'https://fontspark.app/assets/images/share.jpg',
                'intro': "Discover Better Fonts",
                'type':'website',
                'name': 'FontSpark',
                'url': 'https://fontspark.app/',
            },
            {
                'id': 0,
                'image': 'https://static.fontget.com/v/a/varela-round/glyph.png',
                'intro': "Has a variety of fonts available to download and sorted neatly with tags",
                'type':'website',
                'name': 'FontGet',
                'url': 'https://www.fontget.com/',
            },
            {
                'id': 0,
                'image': 'https://fontpair.co/img/instagram-follow.png',
                'intro': "Helps you pair Google Fonts together",
                'type':'website',
                'name': 'FontPair',
                'url': 'https://fontpair.co/',
            },
            {
                'id': 0,
                'image': 'https://tipsmake.com/data/thumbs/review-fontspace-thumb-vaEyGOSbZ.jpg',
                'intro': "A designer-centered free font website that has quick customizable previews",
                'type':'website',
                'name': 'Font Space',
                'url': 'https://www.fontspace.com/',
            },
            {
                'id': 0,
                'image': 'https://www.ecolourprint.co.uk/images/blog/AbstractFonts.png',
                'intro': "Fonts free for personal and commercial use",
                'type':'website',
                'name': 'Abstract Fonts',
                'url': 'http://www.abstractfonts.com/',
            },
            {
                'id': 0,
                'image': 'https://freetypography.com/wp-content/uploads/2021/01/The-brilliant-font-bundle-vol-6-main_desktop.jpg',
                'intro': "A list of high quality fonts",
                'type':'website',
                'name': 'Free Trpography',
                'url': 'https://freetypography.com/',
            },
            {
                'id': 0,
                'image': 'https://i.gzn.jp/img/2019/09/02/leon-sans/02.png',
                'intro': "A geometric sans-serif typeface made with code",
                'type':'website',
                'name': 'Leon Sans',
                'url': 'https://github.com/cmiscm/leonsans/',
            },
            {
                'id': 0,
                'image': 'https://www.lexend.com/static/social/lexend-v2.png',
                'intro': "A variable font empirically shown to significantly improve reading-proficiency",
                'type':'website',
                'name': 'Lexend',
                'url': 'https://www.lexend.com/',
            },
            {
                'id': 0,
                'image': 'https://developer.apple.com/news/images/og/fonts-og-twitter.jpg',
                'intro': "Get the details, frameworks, and tools you need to use system fonts for Apple platforms in your apps",
                'type':'website',
                'name': 'Fonts for Apple Platforms',
                'url': 'https://developer.apple.com/fonts/',
            },
            {
                'id': 0,
                'image': 'https://betterthansuccess.com/wp-content/uploads/2016/06/font-example-1440x720.jpg',
                'intro': "San Francisco Fonts for Windows 10 and non-Apple Platform",
                'type':'website',
                'name': 'SFWin',
                'url': 'https://github.com/blaisck/sfwin/',
            },
            {
                'id': 0,
                'image': 'https://pbs.twimg.com/media/EqKHv1sW8AEzM7-.jpg',
                'intro': "Preview 800+ Google Fonts on top of your own designs, without having to download the fonts",
                'type':'website',
                'name': 'Font Flipper',
                'url': 'https://fontflipper.com/upload',
            },
            {
                'id': 0,
                'image': 'https://miro.medium.com/max/5760/1*54ENACYbQkmnNOrw7yZZDA.png',
                'intro': "Free curated fonts",
                'type':'website',
                'name': 'Fonts Arena',
                'url': 'https://fontsarena.com/',
            },
            {
                'id': 0,
                'image': 'https://www.geckoandfly.com/wp-content/uploads/2017/08/befonts.jpg',
                'intro': "High quality fonts for free",
                'type':'website',
                'name': 'Befonts',
                'url': 'https://befonts.com/',
            },
            {
                'id': 0,
                'image': 'https://arabicfonts.net/fonts/sc_gulf-regular-charmap.png',
                'intro': "Arabic fonts for free",
                'type':'website',
                'name': 'Arabic Fonts',
                'url': 'https://arabicfonts.net/',
            },
            {
                'id': 0,
                'image': 'https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/194bc851403977.58ecb1a5ddfe9.png',
                'intro': "Simple and easy way to view the contents of font files",
                'type':'website',
                'name': 'FontDrop',
                'url': 'https://fontdrop.info/',
            },
            {
                'id': 0,
                'image': 'https://open-foundry.com/img/of-cover-preview.jpg',
                'intro': "FREE platform for curated open-source typefaces",
                'type':'website',
                'name': 'Open Foundary',
                'url': 'https://open-foundry.com/',
            },
            {
                'id': 0,
                'image': 'https://julian-gapp.de/wp-content/uploads/2018/05/1-google-webfont-helper.jpg',
                'intro': "A Hassle-Free Way to Self-Host Google Fonts",
                'type':'website',
                'name': 'Google Webfonts Helper',
                'url': 'https://google-webfonts-helper.herokuapp.com/fonts',
            },
            {
                'id': 0,
                'image': 'https://masterbundles.com/wp-content/uploads/2018/10/Untitled-design-52.png',
                'intro': "When RoughJS meets Font Awesome",
                'type':'website',
                'name': 'Rough Font Awesome',
                'url': 'https://djamshed.github.io/rough-awesome-font/dist/',
            },
            {
                'id': 0,
                'image': 'https://www.whatfontis.com/blog/wp-content/uploads/2020/02/ffonts_net-2.png',
                'intro': "Stylish fonts for free",
                'type':'website',
                'name': 'FFonts',
                'url': 'https://www.ffonts.net/',
            },
            {
                'id': 0,
                'image': 'https://blog.smc.org.in/content/images/2020/05/manjari-zero-tnum-libreoffice.png',
                'intro': "Malayalam fonts for free which are maintained by Swathanthra Malayalam Computing(SMC)",
                'type':'website',
                'name': 'Malayalam Fonts',
                'url': 'https://smc.org.in/fonts/',
            },
            {
                'id': 0,
                'image': 'https://devfonts.gafi.dev/images/preview.jpeg',
                'intro': "find and use the coding fonts for free",
                'type':'website',
                'name': 'Dev Fonts',
                'url': 'https://devfonts.gafi.dev/',
            },
            
        ]
    },


    {
    'image': 'https://i.pinimg.com/originals/41/a3/c5/41a3c51c1a7a7a973da81a119e2db6d3.jpg',
    'type':'websites',
    'name': 'music_asset',
    'start' :
        [
            {
                'id': 0,
                'image': 'https://ichef.bbci.co.uk/news/800/cpsprodpb/2E61/production/_110537811_ec96af27-c995-4ed0-b977-9fb4f1d05d3f.jpg',
                'intro': "The Spinner* is a service that enables you to subconsciously influence a specific person, by controlling the content on the websites he or she usually visits. The targeted person gets repetitively exposed to hundreds of items which are placed and disguised as editorial content.",
                'type':'websites',
                'name': 'thespinner',
                'url': 'https://www.thespinner.net/',
            },
            {
                'id': 0,
                'image': 'https://i1.sndcdn.com/avatars-000042402560-fxpy9a-t500x500.jpg',
                'intro': "PaponeMusic is a music label dedicated to promoting FREE music for the sole purpose of providing creators with the best songs to enhance the creativity",
                'type':'websites',
                'name': 'papone music',
                'url': 'https://www.youtube.com/user/PaponeMusic',
            },
            {
                'id': 0,
                'image': 'https://i1.sndcdn.com/artworks-000105267662-86i42r-t500x500.jpg',
                'intro': "music producer who makes music for everyone to enjoy and use for free. No charges! Please credit me in the description of your Youtube videos! If you ",
                'type':'websites',
                'name': 'HolFix - Royalty Free Music',
                'url': 'https://www.youtube.com/user/holfix',
            },
            {
                'id': 0,
                'image': '  https://i1.sndcdn.com/artworks-000102769935-nkultb-t500x500.jpg',
                'intro': "NoCopyrightSounds is a copyright free / stream safe record label, providing free to use music to the content creator community. We work with artists from around the globe",
                'type':'websites',
                'name': 'NoCopyrightSounds',
                'url': 'https://www.youtube.com/user/NoCopyrightSounds',
            },
            {
                'id': 0,
                'image': 'http://dig.ccmixter.org/images/logo.png',
                'intro': "NoCopyrightSounds is a copyright free / stream safe record label, providing free to use music to the content creator community. We work with artists from around the globe",
                'type':'websites',
                'name': 'NoCopyrightSounds',
                'url': 'http://dig.ccmixter.org/',
            },
            {
                'id': 0,
                'image': 'https://incompetech.com/wordpress/wp-content/uploads/2015/02/2013janlogo.png',
                'intro': "royality free music",
                'type':'websites',
                'name': 'incompetech',
                'url': 'hhttps://incompetech.com/',
            },
            {
                'id': 0,
                'image': 'https://offeo.com/learn/wp-content/uploads/2019/03/freeplay-music.jpg',
                'intro': "OVER 50,000 SONGS FREE FOR youtube AND MORE",
                'type':'websites',
                'name': 'incompetech',
                'url': 'https://freeplaymusic.com/#/',
            },
        ]
    },

    {
        'image':'https://cdn.logo.com/hotlink-ok/logo-social.png',
        'type':'websites',
        'name': 'Logo',
        'start': 
        [
            {     
                'id': 0,
                'image':'https://www.namecheap.com/status-updates/wp-content/themes/namecheap-wp-theme/images/logo.png',
                'intro': 'Fast, All-in-One Logo Generator',
                'type':'website',
                'name': 'Free Logo Maker',
                'url': 'https://www.namecheap.com/logo-maker/',
            },
            {     
                'id': 0,
                'image':'https://www.thesmbguide.com/images/logomakr-1024x512-20190717.png',
                'intro': 'Create custom logos',
                'type':'website',
                'name': 'Logo Makr',
                'url': 'https://logomakr.com/',
            },
            {     
                'id': 0,
                'image':'https://cdn.worldvectorlogo.com/logos/worldvectorlogo.svg',
                'intro': 'Download vector logos of brands you love',
                'type':'website',
                'name': 'World Vector Logo',
                'url': 'https://worldvectorlogo.com/',
            },
            {     
                'id': 0,
                'image':'https://www.vectorlogo.zone/images/about/vlzlogo-grey.svg',
                'intro': 'consistently formatted SVG logos',
                'type':'website',
                'name': 'VectorLogoZone',
                'url': 'https://www.vectorlogo.zone/',
            },
            {     
                'id': 0,
                'image': 'https://cdn.vectorguru.org/wp-content/uploads/2017/07/Freelogovector-Popular-1024x534.jpg',
                'intro': 'Generate and download your logo for free in PNG and SVG format',
                'type':'website',
                'name': 'LogoHub',
                'url': 'https://logohub.io/',
            },
            {     
                'id': 0,
                'image':'https://www.sketchappsources.com/resources/source-image/browser-icons-kyenlee.jpg',
                'intro': 'High resolution web browser logos',
                'type':'website',
                'name': 'Browser Logo',
                'url': 'https://github.com/alrra/browser-logos/',
            },
            {     
                'id': 0,
                'image':'https://speckyboy.com/wp-content/uploads/2016/02/free-payment-method-gateway-icon-sets-13.png',
                'intro': 'Logos for payment systems available in png and svg',
                'type':'websites',
                'name': 'Payment System Logos',
                'url': 'https://github.com/mpay24/payment-logos/',
            },
            {     
                'id': 0,
                'image':'https://cms-assets.tutsplus.com/uploads/users/30/posts/27050/image/svgporn.png',
                'intro': '1000+ high-quality SVG logos',
                'type':'website',
                'name': 'SVG Porn',
                'url': 'https://svgporn.com/',
            },
            {     
                'id': 0,
                'image':'https://logosear.ch/images/hero.png',
                'intro': 'search engine with over 200,000 SVG logos indexed',
                'type':'website',
                'name': 'LogoSear.ch',
                'url':'https://logosear.ch/search.html',
            },
            {                 
                'id': 0,
                'image':'https://d16kg6xo62zbe.cloudfront.net/site-picture/463x256/i/instantlogosearch.com.png',
                'intro': 'thousands of free brands logos ( SVG - PNG )',
                'type':'website',
                'name': 'Instant Logo Search',
                'url':'http://instantlogosearch.com/',

            },
      
            {
                'id': 0,
                'image':'https://images.ctfassets.net/aq13lwl6616q/1bqjiu41cA1kJS6x9cQzXr/ef7072cfccbae7af67591f332207e06a/fiverr-logo-new-green-64920d4e75a1e04f4fc7988365357c16.png',
                'intro': 'Make a Free Logo that matches your look & feel in 5 min and only pay when satisfied!',
                'type':'website',
                'name': 'Fiverr logo maker',
                'url':'https://www.squarespace.com/logo#N4IghgrgLgFgpgExALgGZgDYGc4F8gAA',

            },
            {
                'id': 0,
                'image':'https://images.ctfassets.net/aq13lwl6616q/1bqjiu41cA1kJS6x9cQzXr/ef7072cfccbae7af67591f332207e06a/fiverr-logo-new-green-64920d4e75a1e04f4fc7988365357c16.png',
                'intro': 'Make a Free Logo that matches your look & feel in 5 min and only pay when satisfied!',
                'type':'website',
                'name': 'Fiverr logo maker',
                'url':'https://www.squarespace.com/logo#N4IghgrgLgFgpgExALgGZgDYGc4F8gAA',

            },
            {
                'id': 0,
                'image':'https://images.ctfassets.net/aq13lwl6616q/395InwAs6M2FAyXD21s0Lo/0ca13306b6dbb2b03e0ba6429a9b5440/namecheap_img.png',
                'intro': 'Create a free professional logo in minutes',
                'type':'website',
                'name': 'Namecheaps Free Logo Maker',
                'url':'https://www.namecheap.com/logo-maker/',

            },
            {
                'id': 0,
                'image':'https://images.ctfassets.net/aq13lwl6616q/395InwAs6M2FAyXD21s0Lo/0ca13306b6dbb2b03e0ba6429a9b5440/namecheap_img.png',
                'intro': 'Create a free professional logo in minutes',
                'type':'website',
                'name': 'Namecheaps Free Logo Maker',
                'url':'https://www.namecheap.com/logo-maker/',

            },
        ]
    },

    {
        'image':'https://www.prolore.com/blog/wp-content/uploads/2015/08/favicon-680x400.jpg',
        'type':'websites',
        'name': 'Favicons',
        'start': 
        [
            {     
                'id': 0,
                'image':'https://www.jerriepelser.com/static/09b8a45c9f5d9869745e958914560fde/b97f6/favicon-generator.png',
                'intro': 'Generate favicons and images from Font Awesome icons',
                'type':'website',
                'name': 'Gauger',
                'url': 'https://gauger.io/fonticon/',
            },
            {     
                'id': 0,
                'image':'https://realfavicongenerator.net/favicon_generator_og_image.png',
                'intro': 'Generate icons for all platforms (Windows, iOS, Android)',
                'type':'website',
                'name': 'RealFaviconGenerator',
                'url': 'https://realfavicongenerator.net/',
            },
            {     
                'id': 0,
                'image': 'https://searchenginereports.net/newassets/og_images/favicon-generator-tool.png',
                'intro': 'Generate favicon ico files for your website',
                'type':'website',
                'name': 'Faviocn Generator',
                'url': 'http://tools.dynamicdrive.com/favicon/',
            },
            {     
                'id': 0,
                'image': 'https://din1rx1owsiuu.cloudfront.net/screens/pc-landscape/www.favicomatic.com.jpg',
                'intro': 'Generate favicons of all the sizes and formats as well as the HTML code needed to support every possible browser or device',
                'type':'website',
                'name': 'Favicomatic',
                'url': 'https://favicomatic.com/',
            },
            {     
                'id': 0,
                'image':'https://favicon.io/og-image.png',
                'intro': 'Generate a favicon from text, from an image, or from an emoji. Download in .ico and .png formats',
                'type':'website',
                'name': 'Favicon.io',
                'url': 'https://favicon.io/',
            },
            
        ]
    },

    {
        'image':'https://cdn.presslabs.com/wp-content/uploads/2016/04/Blog_Presslabs-Webicons_V1.png',
        'type':'websites',
        'name': 'Icon Fonts',
        'start': 
        [
            {     
                'id': 0,
                'image': 'https://figmaelements.com/wp-content/uploads/2020/10/heroicons.png',
                'intro': 'Free Open Source Svg Icon Library',
                'type':'website',
                'name': 'Hero Icons',
                'url': 'https://heroicons.dev/',
            },
            {     
                'id': 0,
                'image': 'https://vectorified.com/images/font-awesome-search-icon-29.png',
                'intro': 'It is a free alternative for Font Awesome, flat icons that offer complete coverage of the main Font Awesome icon set.',
                'type':'website',
                'name': 'Line Awesome',
                'url': 'https://icons8.com/line-awesome',
            },
            {     
                'id': 0,
                'image': 'https://storage.pixteller.com/designs/designs-images/2020-06-17/05/41-mobiriseicons-1-5eea29aed59d8.png',
                'intro': 'A free, open source set of 150 elegant, pixel-perfect linear icons, available as web icon font and SVG icons.',
                'type':'website',
                'name': 'Mobirise Icons',
                'url': 'https://mobiriseicons.com/',
            },
            {     
                'id': 0,
                'image': 'https://iconset.io/sets/unicons.svg',
                'intro': 'A set of 1100+ Free line style icons available as web font, SVG icons, and as components for JS frameworks like React, Vue and React Native.',
                'type':'website',
                'name': 'Unicons',
                'url': 'https://iconscout.com/unicons',
            },
            {     
                'id': 0,
                'image': 'https://linea.io/wp-content/uploads/2020/03/basic-Icons-1024x246.png',
                'intro': 'Linea: Featuring 750+ Free Icons',
                'type':'website',
                'name': 'Linea Icon',
                'url': 'https://linea.io/',
            },
            {     
                'id': 0,
                'image': 'https://css-tricks.com/wp-content/uploads/2013/10/fontello.jpg',
                'intro': '200+ web icons where you can customize the names or codes of icons.',
                'type':'website',
                'name': 'Fontello',
                'url': 'https://fontello.com/',
            },
            {     
                'id': 0,
                'image': 'https://domain.me/wp-content/uploads/2013/09/fontastic-main-pic.png',
                'intro': 'Create your custom icon fonts in seconds. Over 9,000 icons available to pick from or upload your custom svg',
                'type':'website',
                'name': 'Fontastic.me',
                'url': 'http://fontastic.me/',
            },
            {     
                'id': 0,
                'image': 'https://i.pinimg.com/originals/cd/5d/61/cd5d6182e6fd7f0a501410147bbd7553.png',
                'intro': '890+ handcrafted icons to make your web app awesome',
                'type':'website',
                'name': 'Jam Icons',
                'url': 'https://jam-icons.com/',
            },
            {     
                'id': 0,
                'image': 'https://cdn.freebiesbug.com/wp-content/uploads/2014/03/icon-font-pack-thin-stroke-tab-bar-ios-7-html-580x435.jpg',
                'intro': '202 thin stroke icons inspired by iOS 7',
                'type':'website',
                'name': 'Stroke 7',
                'url': 'https://themes-pixeden.com/font-demos/7-stroke/index.html',
            },
            {     
                'id': 0,
                'image': 'https://unblast.com/wp-content/uploads/2018/06/Weather-Icons.jpg',
                'intro': 'Weather Icons is the only icon font with 222 weather themed icons',
                'type':'website',
                'name': 'Weather Icons',
                'url': 'https://erikflowers.github.io/weather-icons/',
            },
            {     
                'id': 0,
                'image': 'https://speckyboy.com/wp-content/uploads/2016/02/free-payment-method-gateway-icon-sets-05.png',
                'intro': 'A sleek web font for payment operators and methods. Featuring 116 icons',
                'type':'website',
                'name': 'PaymentFont',
                'url': 'https://github.com/AlexanderPoellmann/PaymentFont',
            },
            {     
                'id': 0,
                'image': 'https://psddd.co/wp-content/uploads/2017/06/DevIcon.png',
                'intro': 'Devicon is a set of icons representing programming languages, designing & development tools',
                'type':'website',
                'name': 'Devicon',
                'url': 'https://devicon.dev/',
            },
            {     
                'id': 0,
                'image': 'https://user-images.githubusercontent.com/35271042/89581770-6b429200-d7ec-11ea-8905-7f19c6c57aae.png',
                'intro': 'The icon font from Visual Studio Code',
                'type':'website',
                'name': 'Vscode Codicons',
                'url': 'https://microsoft.github.io/vscode-codicons/dist/codicon.html',
            },
            {     
                'id': 0,
                'image': 'https://zavoloklom.github.io/material-design-iconic-font/img/Material-Design-Iconic-Font-2.png',
                'intro': 'Material design icon font',
                'type':'website',
                'name': 'Material Design Icon Font',
                'url': 'http://zavoloklom.github.io/material-design-iconic-font/index.html',
            },
            {     
                'id': 0,
                'image': 'https://materialpalettes.com/images/og-image.jpg',
                'intro': 'Free to pick palettes, icons and colors for Material Design]',
                'type':'website',
                'name': 'Material Palette',
                'url': 'https://www.materialpalette.com/icons',
            },
            {     
                'id': 0,
                'image': 'https://icofont.com/images/og/icons.jpg',
                'intro': '2100+ free icons to spice up your creative designs',
                'type':'website',
                'name': 'Icofont',
                'url': 'https://icofont.com/',
            },
            {     
                'id': 0,
                'image': 'https://theprotoolbox.com/wp-content/uploads/2020/04/box-icons-vectors-free-set.png',
                'intro': 'Boxicons is a free collection of carefully crafted open source icons',
                'type':'website',
                'name': 'Boxicons',
                'url': 'https://boxicons.com/',
            },
            {     
                'id': 0,
                'image': 'https://i.redd.it/cv5yizua23601.jpg',
                'intro': 'Fontisto the iconic font and css toolkit · 616+ free icons',
                'type':'website',
                'name': 'fontisto.com',
                'url': 'https://fontisto.com/',
            },
            {     
                'id': 0,
                'image':'https://zurb.com/blog/system/images/1221/original/Foundation5.jpg',
                'intro': 'Customizable Foundation icons',
                'type':'website',
                'name': 'Zurb Foundation Icons',
                'url': 'https://zurb.com/playground/foundation-icon-fonts-3',
            },
            {     
                'id': 0,
                'image':'https://mockupless.com/assets/img/ionicons-ef6c1f66-f3cc-4b2a-8502-96a4b72316d6.006ea8bf.png',
                'intro': 'Beautifully crafted open source icons from Ionic team',
                'type':'website',
                'name': 'IonIcons',
                'url': 'https://ionicons.com/',
            },
            {     
                'id': 0,
                'image': 'https://techcrunch.com/wp-content/uploads/2018/05/screenshot-materialio.png',
                'intro': 'Material design icon library',
                'type':'website',
                'name': 'Material.io',
                'url': 'https://material.io/resources/icons/?style=baseline',
            },
            {     
                'id': 0,
                'image': 'https://vectorified.com/images/font-awesome-search-icon-29.png',
                'intro': 'Swap in replacement of Font Awesome with modern line icons',
                'type': 'website',
                'name': 'Line Awesome',
                'url': 'https://icons8.com/line-awesome',
            },
            {     
                'id': 0,
                'image': 'https://fontawesome.com/images/docs/web-icons-gallery-2.png',
                'intro': "The web's most popular icon set and toolkit",
                'type':'website',
                'name': 'Font Awesome',
                'url': 'https://fontawesome.com/',
            },
            
            
        ]
    },

    {
        'image': 'https://devassets.com/img/dev-assets-promo.jpg',
        'name': 'free_developer_assets',
        'type':'astes',
        'start' : [
            {
                'id': 0,
        'image': 'desktop_4x.png',
        'intro': '3d Illustrations and freebies. We make products that help designers work faster and be more efficient.',
        'name': 'wannathis.one',
        'url': 'https://wannathis.one',
        
        'price': 'free',
        'type': "Illustrations 3d",
            },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/1LbokUAQ0rQgQTuX1z93zk/291d0a604dcf55e8068425ade74d1a5e/professions-avatars.png',
        'intro': 'GIGrowing library of free avatar illustrations. Use them royalty-free for your commercial or personal ',
        'name': 'Ultimate Avatar Library',
        'url': 'https://limitlessdesigns.io/avatar-illustrations',
        
        'price': 'free',
        'type': "avatar",
    },
    {
        'id': 0,
        'image': 'https://background-generator.com/layout_thumbs/1.png',
        'intro': 'Make cool, free backgrounds quickly for your project with this easy to use tool.',
        'name': 'Background Generator',
        'url': 'https://background-generator.com/',
        'type': 'background generator',
        'price': 'free',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/11LBC9qMWMFoQd4HzkFoQL/f8b485951af22e3d47b81cae07c6335e/image.png',
        'intro': 'Free vector illustrations to class up your project',
        'name': 'Free Vector Illustrations',
        'url': 'https://icons8.com/illustrations',
        'type': 'free illustrations',
        'price': 'free',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/15CE9nlVDqJdcGZjgfAtsN/c9fc44c9eafa17d9e1eb606b28a9f732/image.png',
        'intro': 'Beautiful, free art and illustrations available for commercial use.',
        'name': 'Free Stock Illustrations',
        'url': 'https://mixkit.co/art/',
        'type': 'illustrations',
        'price': 'free',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/6As3uO6qMDulI1hXHPHG3e/2200acd27a4122fa8a7745853911a4ed/image.png',
        'intro': 'A collection of free images for landing pages.',
        'name': 'LandingStock',
        'url': 'https://landingstock.com/',
        'type': 'illustrations',
        'price': 'free',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/22axf05qxm9dQbAbbYtLaH/d5c67f33edc640b35abb54bf5feff24c/image.png',
        'intro': 'Free collection of beautiful, customizable patterns for all vector formats.',
        'name': 'Beautiful & Customizable Patterns',
        'url': 'https://lstore.graphics/paaatterns/',
        'type': 'illustrations',
        'price': 'free',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/3wJpjVIhvOjtmbqQp6JpdI/5ec308fbb5055b4f2882518cdfadcfde/image.png',
        'intro': 'Royalty-free designs for your website, social media, blog, and email newsletters.',
        'name': 'Royalty Free Designs',
        'url': 'https://getwaves.io/',
        'type': 'illustrations',
        'price': 'free',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5EJ5x6MtYpfEWBY0FY2hUi/379b3947ca4d2b47a3541a1113bd05cf/getwaves-cover-a91094679addf32c17ee7fb66d5f8215.jpg?w=786&h=443&q=50&fm=webp',
        'intro': 'A free SVG wave generator to make unique SVG waves for your next web design.',
        'name': 'Svg wave generator',
        'url': 'https://delesign.com/free-designs/graphics/',
        'type': 'illustrations',
        'price': 'free',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5p24UI5cVtJierhSmaopzt/c2394a30ae7d2800067f781019ab10c9/image.png',
        'intro': 'Collection of illustrations that you can use for your websites 404 page.',
        'name': '404 Illustrations',
        'url': 'https://www.kapwing.com/404-illustrations',
        'type': 'illustrations',
        'price': 'free',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/18O3O4VWUt1QndX1JFdSC9/e175401b14981419f38ed0488623a805/image.png',
        'intro': 'Free paper illustrations for personal or commercial use.',
        'name': 'Paper Illustrations',
        'url': 'https://iconscout.com/paper-illustrations',
        'type': 'illustrations',
        'price': 'free',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/1qBOtbcmoTeaZ4rNRdsAhe/64954cd609c9419dc9345112b5cb5563/5e51ce05258ffe802886ef21_cover-1.png',
        'intro': 'Open Peeps is a hand-drawn illustration library to create scenes of people.',
        'name': 'Hand-Drawn Illustration Library',
        'url': 'https://www.openpeeps.com/',
        'type': 'illustrations',
        'price': 'free',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/4et82Ql1pqOAkmLKddAjXo/ded0c3cd3bf7fc09d0ea7519acf6dc21/image.png',
        'intro': 'Colors & Fonts is a curated library of colors and fonts for digital designers and web developers.',
        'name': 'Paper Illustrations',
        'url': 'https://www.colorsandfonts.com/',
        'type': 'illustrations',
        'price': 'free',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/7tUYkp5C3ZqF0kZxxAEhTC/1a11bd19e8dcd401ba38cc69305dc127/image.png',
        'intro': 'Find, Vote, Save, Share your favorite design tools!',
        'name': 'Ultimate Design Tools Depository',
        'url': 'https://www.designvalley.club/',
        'type': 'illustrations',
        'price': 'free',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/1JRFwk2fZ0CMZggKjzpH61/acfaa773b892e5d6caea40e44beca4f2/image.png',
        'intro': 'MIT licensed (free for personal or commerical) SVG illustration images in different shapes & styles.',
        'name': 'Free Illustrations & Icons',
        'url': 'https://lukaszadam.com/illustrations',
        'type': 'illustrations',
        'price': 'free',
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/2dryfsoBtiKn5Nblx9FIVW/7526bcb9a502f224854573ab9a6509ce/image.png',
        'intro': 'Gives you real world examples as to how your colors could be used in your projects.',
        'name': 'Curated Colors in Context',
        'url': 'https://www.happyhues.co/',
        'type': 'illustrations',
        'price': 'free',
    },
    
    
]
    },
    {
        'image':'https://marionettestudio.com/wp-content/uploads/2016/11/22-despicable-me-2-animation-movie.jpg',
        
        'name': 'animation_images',
        'start': [
    {
        
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/3aqr7XDogg9jcGnUglJYOt/05488b640b4307bf3a2e96259bc9bd39/image.png',
        'intro': 'Free resource of 100k high-quality faces, each entirely generated by AI.',
        'name': '100,000 AI-Generated Faces',
        'type': "Ai Photos",
        'url': 'https://generated.photos/'
    
    },
    {
        'id': 0,
        'image': 'https://static.lottiefiles.com/images/og_img.jpg',
        'intro': 'Lottie animations and the tools you need to test and perfect them. Simply edit and ship your animations in just a few clicks.',
        'name': 'lottie',
        'type': "aniamtion",
        'url': 'https://lottiefiles.com/featured'
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5c05205a90375ebb9d52fad7_Image-p-1600.jpeg',
        'intro': 'Mix-&-match illustrations of people with a design library',
        'name': 'Hummans',
        'type': "Human illustrations",
        'url': 'https://www.humaaans.com/?ref=producthunt'
    },
    
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b9f720f08470e3f35fac2cd_undraw_upload_87y9%20(1).svg',
'intro': "Browse to find the images that fit your needs and click to download. Take advantage of the on-the-fly color image generation to match your brand identity.",
'name': 'UnDraw',
'url':'https://undraw.co/illustrations',
'price': 'free',
'type': 'Illustartions'
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9bea6e87a4d000109dbd1_jakub-dziubak-394720-(1).jpg',
        'intro': 'Beautiful high quality free images and photos you can download and use for any project. No attribution required.',
        'name': 'unsplash',
        'url': 'https://unsplash.com/',
        'price': 'free',
        'type': "photos",
    },
    {
        'id': 0,
        'image': 'https://www.logo-designer.co/wp-content/uploads/2013/09/iStock-logo-design-identity-getty-images-Build.jpg',
        'intro': 'free photos',
        'name': 'istock',
        'url': 'https://www.istockphoto.com/collaboration/boards/L9m43WDlbUO8O94wqUFIIA',
        'extra': 'Human illustrations',
        'price': 'price',
        'type': "Photos",
    },
    {
        'id': 0,
        'image': 'https://illlustrations.co/notebook.png',
        'intro': 'Designed 100 awesome illustrations during 100 days of illustration challenge (Now added more than 120+ illustrations). You can download all illustrations completely free and use these to design awesome - landing pages, mobile app or presentations.',
        'name': 'illustration.co',
        'url': 'https://illlustrations.co/',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "Photos",
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/22Ou5s2XiiP6SlL9pZg68a/64957a5a1aee0ccaca08b30c65ee94ab/image.png',
        'intro': 'High quality, royalty free video footage and art.',
        'name': 'Free Video Footage, Update Daily',
        'url': 'https://mixkit.co/',
        'extra': 'videos daily',
        'price': 'free',
        'type': "videos",
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/2qhSA5GyzwhG0WpUYJjb51/a9223b2026797a52c9d6187da61f907c/image.png?w=800&h=413&q=50&fm=webp',
        'intro': 'Royalty free (personal or commercial use), unique and beautiful video footage.',
        'name': 'Royalty Free Video Footage',
        'url': 'https://coverr.co/',
        'extra': 'photos daily',
        'price': 'free',
        'type': "photos",
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/4ZkTkQZHZsd1FdnwJ2oeiF/c699c7ed50d4ee7905d5f759fca4efe3/image.png',
        'intro': 'Free stock footage for your website, promo video or anything else..',
        'name': 'Free Stock Video Footage',
        'url': 'https://www.pexels.com/videos',
        'extra': 'photos daily',
        'price': 'free',
        'type': "photod",
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5wB8gtukadk7CMWmMuAhuk/3d8ed5be50859e924270db679f329707/image.png?w=175&h=131&q=50&fm=webp',
        'intro': 'Animals, people, landscapes, buildings. Find illustrations by artist, title of book or periodical.',
        'name': 'Old Book Illustrations',
        'url': 'https://www.oldbookillustrations.com/',
        'extra': 'photos daily',
        'price': 'free',
        'type': "photo",
    }, 
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/SSCSWWFQCXndWa3sy7G6l/d29788e796598b065dc772b0f90df355/Blog-Featured-Images-Dec-2019-11.jpg?w=700&h=400&q=50&fm=webp',
        'intro': 'Free deliver localized, personalized photography stock photos for Digital Marketing.',
        'name': 'Royalty-Free Stock Photos',
        'url': 'https://www.shotzr.com/',
        'extra': 'photos daily',
        'price': 'free',
        'type': "photo",
    }, 
    {
        'id': 0,
        'image': 'https://giphy.com/static/img/giphy_logo_square_social.png',
        'intro': 'GIPHY is your top source for the best & newest GIFs & Animated Stickers online. Find everything from funny GIFs, reaction GIFs, unique GIFs and more',
        'name': 'giphy.com',
        'url': 'https://giphy.com/',
        'extra': 'Giphy',
        'price': 'free',
        'type': "gifs",
    },
    

]
    },
    {
        'image': 'https://betterthansuccess.com/wp-content/uploads/2016/06/font-example-1440x720.jpg',
        'name': 'font',
        'start' : [
    {
'id': 0,
'image':'https://images.ctfassets.net/aq13lwl6616q/4oMoXn0XeYnYcLbwzBLZeS/ad36c11f691a21c977fe8c1a1719c47b/fontpairings-social-thumb.jpg?w=800&h=420&q=50&fm=webp',
'intro': 'Create and test amazing font pair combinations and see how they look in your project.',
'name': '99 Font Pairings & Typeface Combinations',
'url':'https://fontpairings.bypeople.com/',
'type':'font website',

    },
    {
'id': 0,
'image':'https://miro.medium.com/max/3620/1*zC9oF9BOxoV6acjfho1lPg.png',
'intro': 'A fancy cool ✅ font generator that helps create stylish text font styles with beautiful symbols and fancy characters for social networks & any other places.',
'name': 'cool fancy symbol',
'url':'https://coolsymbol.com/cool-fancy-text-generator.html',
'type':'font website',

    },
    {
'id': 1,
'image': 'https://www.dafont.com/img/charmap/m/o/moonbright0.png',
'intro':'Archive of freely downloadable fonts. Browse by alphabetical listing, by style, by author or by popularity.',
'name': 'dafront.com',
'url': 'https://www.dafont.com/base-02.font',
'type':'font website',

    }
    ,
    {
'id': 2,
'image': 'https://www.fontmirror.com/app_public/logo/fontmirror-promotional-cover-bg.png',
'intro': 'Free download digital fonts. Get TTF, OTF or ZIP. Free for commercial use fonts, and more.',
'name': 'font mirror',
'url': 'https://www.fontmirror.com',
'type':'font website',

    }
    ,
    {
'id': 3,
'image': 'https://il.static.1001fonts.net/g/i/gisbon-demo-font-2-big.jpeg',
'intro': '23232 free fonts in 12468 families · Free licenses for commercial use · Direct font downloads',
'name': '101 fonts',
'url': 'https://www.1001fonts.com/signature-fonts.html',
'type':'font website',

    }
    ,
    {
'id': 4,
'image': "https://fontspace.imgix.net/static/fontspace-logo-white-text.svg",
'intro': 'Free downloads of legally licensed fonts that are perfect for your design projects. The best place in the universe to search for amazing fonts.',
'name': 'fontspace',
'url': 'https://www.fontspace.com/category/shadow',
'type':'font website',

    }
    ,
    {
'id':5 ,
'image':'https://asistatic.azureedge.net/images/fontflipper.com.jpeg',
'intro': 'https://fontflipper.com/canvas-editor',
'name': 'font flipper',
'url': 'https://fontflipper.com/canvas-editor',
'type':'font website',
    }
]
    },
{
    'image': 'https://ceblog.s3.amazonaws.com/wp-content/uploads/2018/10/25102730/best-colors-websites-3.png',
    'name': 'colors',
'start': [
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
'extra': 'colors pallet',
'price': 'free',
'type': 'Resources'
    },
]
},

{
    'image': 'https://benjweinberg.files.wordpress.com/2017/08/what-is-an-definite-and-indefinite-articles-hd.png',
    'name': 'Artices',
    'start': [
    
        
            
                {
        'id': 0,
        'image': 'https://miro.medium.com/max/1909/1*ywYwvB-aydv0Ovx7K-5P3g.jpeg',
        'intro': "A new take on the age-old question: Should you rewrite your application from scratch, or is that “the single worst strategic mistake that any software company can make”? ",
        'name': 'Lessons from 6 software rewrite stories',
        'type': 'Artices',
        'url': 'https://medium.com/@herbcaudill/lessons-from-6-software-rewrite-stories-635e4c8f7c22',
        },
    {
        'id': 0,
        'type': 'Artices',
        'image': 'https://cdn-media-1.freecodecamp.org/images/1*3pyJUEclXtPt8TNONerTUg.jpeg',
        'intro': "How to escape tutorial purgatory as a new developer — or at any time in your career.",
        'name': 'For a long time I held off from starting my own side projects because of how much I didn’t know how to do.',
        'url': 'https://www.freecodecamp.org/news/how-to-escape-tutorial-purgatory-as-a-new-developer-or-at-any-time-in-your-career-e3a4b2384a40/',
    },
    {
        'id': 0,
        'type': 'Artices',
        'image': 'https://cdn-media-1.freecodecamp.org/images/1*3pyJUEclXtPt8TNONerTUg.jpeg',
        'intro': "How to escape tutorial purgatory as a new developer — or at any time in your career.",
        'name': 'For a long time I held off from starting my own side projects because of how much I didn’t know how to do.',
        'url': 'https://www.freecodecamp.org/news/how-to-escape-tutorial-purgatory-as-a-new-developer-or-at-any-time-in-your-career-e3a4b2384a40/',
    },
    {
        'id': 0,
        'type': 'Artices',
        'image': 'https://cdn-media-1.freecodecamp.org/images/1*3pyJUEclXtPt8TNONerTUg.jpeg',
        'intro': "How to escape tutorial purgatory as a new developer — or at any time in your career.",
        'name': 'For a long time I held off from starting my own side projects because of how much I didn’t know how to do.',
        'url': 'https://www.freecodecamp.org/news/how-to-escape-tutorial-purgatory-as-a-new-developer-or-at-any-time-in-your-career-e3a4b2384a40/',
    },
            
      
    
]
},
{
    'image' : 'https://media.geeksforgeeks.org/wp-content/cdn-uploads/20191213191344/Why-Data-Structures-and-Algorithms-Are-Important-to-Learn.png',
    'name': 'DataStructures_Algorithms',
    'start': [
    {
        'id': 0,
        'image': 'https://www.telcoma.in/en/wp-content/uploads/2019/09/Mastering-Data-Structures-Algorithms-using-C-and-C0-.jpg',
        'intro': "Download Free Your Desired AppIntroduction to Algorithms Introduction to course. Why we write Algorithm? Who writes Algorithm? When Algorithms are written? Differences between Algorithms and Programs",
        'type': "Youtube videos",
        'name': 'Abdul Bari: YouTubeChannel for Algorithms',
        'url': 'https://www.youtube.com/watch?v=0IAPZzGSbME&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=2&t=0s',
    },
    {
        'id': 0,
        'image': 'https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190529171221/Learning-Data-Structures-and-Algorithms-is-Important1-1024x424.png',
        'intro': "Hey guys, we have created this channel to provide quality education to students who want to learn, grow and do something beautiful with their life",
        'type': "Youtube videos",
        'name': 'Data Structures and algorithms',
        'url': 'https://www.youtube.com/watch?v=lxja8wBwN0k&list=PLKKfKV1b9e8ps6dD3QA5KFfHdiWj9cB1s',
    },
    {
        'id': 0,
        'image': 'https://miro.medium.com/max/1024/1*9QRFQdpO2f59GsN2KsE9XA.png',
        'intro': "Data Structure & Algorithms course is the most easiest way, that also at free of cost. This playlist has been created by WsCube Tech to help you learn and understand the concepts of Data Structure Algorithm(DSA). All videos cover a wide range of topics and explain each topic with practical examples. You can easily learn about Data Structure Algorithm(DSA), Subscribe the channel to get the latest videos. ",
        'type': "Youtube videos(Hindi)",
        'name': 'Data Structures and algorithms Course',
        'url': 'https://www.youtube.com/playlist?list=PLmGElG-9wxc9Us6IK6Qy-KHlG_F3IS6Q9',
    },
    {
        'id': 0,
        'image': 'https://miro.medium.com/max/1024/1*9QRFQdpO2f59GsN2KsE9XA.pnghttps://i.ytimg.com/vi/CvSOaYi89B4/maxresdefault.jpg',
        'intro': "What are algorithms and why should you care? We'll start with an overview of algorithms and then discuss two games that you could use an algorithm to solve more efficiently - the number guessing game and a route-finding game.",
        'type': "videos + exersise",
        'name': 'Khan Academy',
        'url': 'https://www.khanacademy.org/computing/computer-science/algorithms',
    },
    {
        'id': 0,
        'image': 'https://miro.medium.com/max/1000/0*ZzOeJHpQQk4RhhWW.png',
        'intro': " Pre-requisite for this lesson is good understanding of pointers in C. In this series of lessons, we will study and implement data structures. We will be implementing these data structures in c or c++.  Pre-requisite for this lesson is good understanding of pointers in C. Watch this series on pointers before starting on this series: ",
        'type': "Youtube videos",
        'name': 'Data structures by mycodeschool',
        'url': 'https://www.youtube.com/playlist?list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P',
    },

]
}
,
{
    'image': 'https://www.thebalancecareers.com/thmb/EzVIPY9EHd15iMMBUVwJVjIM0jI=/735x0/ScreenShot2019-08-13at12.32.30PM-a5be9aa6e07f4b1381ff525cf7a3ecad.png',
    'name':'Graphic_deginer',
    'start': [
    {
        'id': 0,
        'image': 'https://speckyboy.com/wp-content/uploads/2019/02/free-adobe-premier-pro-video-templates-01.jpg',
        'intro': "Video is a great way to build trust with potential clients, showcase your products in use, and add a touch of personality to your brand. But if you want to achieve results with video marketing, you need to make sure your videos stand out from the competition.",
        'type': "Free motion graphic templates",
        'name': 'speckybou',
        'url': 'https://speckyboy.com/free-templates-adobe-premier-pro/',
    },
    {
        'id': 0,
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/ira-design.jpg',
        'intro': "Ira Design is a free and open-source illustration tool developed by Creative Tim that help designers to build their own amazing illustrations using awesome gradients and hand-drawn sketch components.",
        'type': "Free motion graphic templates",
        'name': 'Ira Design ',
        'url': 'https://iradesign.io/?ref=creativetim',
    },
    {
        'id': 0,
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/stubborn-generator-768x576.png',
        'intro': "Stubborn is a generator for customizable illustrations that can help you:",
        'type': "illustration creator",
        'name': 'stburn generator',
        'url': 'https://stubborn.fun/',
    },
    {
        'id': 0,
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/vector-creator-768x480.jpeg',
        'intro': "Vector Illustration Creator is a free tool for creating illustrations with no need for design teamwork.",
        'type': "Illustartion creator",
        'name': 'Vector Illustration Creator',
        'url': 'https://icons8.com/vector-creator',
    },
    {
        'id': 0,
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/unnamed-file-768x363.jpg',
        'intro': "Gravit Designer is a full-featured, vector graphic design solution for designers. The program provides a set of powerful tools that help the user to unleash true creativity in designing beautiful and detailed vector imagery. It is suitable for:",
        'type': "Free motion graphic templates",
        'name': 'Gravit designer',
        'url': 'https://www.designer.io/en/',
    },
    {
        'id': 0,
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/smash-768x403.png',
        'intro': "Smash Illustration Is a very nice free illustration constructor that offers more than 250 illustrations ready to help you create unique scenes.",
        'type': "Free motion graphic templates",
        'name': 'Smash Illustration ',
        'url': 'https://usesmash.com/',
    },
]
}

]







freesoftware = [
 {
     'name':'free_courses',
     'image': 'https://www.learningcrux.com/logo-dark.png',
    'intro': "Download free udemy+skillshare+individual+and more courses free of costs",
     'start':[
    {
        'id': 0,
        'image': 'https://freecoursesite.com/wp-content/uploads/2018/03/hjhjh.png',
        'intro': "Download free udemy+skillshare+individual+and more courses free of costs",
        'type': "Downoload free ",
        'name': 'freecoursesites (illegal)',
        'url': 'https://freecoursesite.com/',
    }
    ,
    {
        'id': 0,
        'image': 'https://www.learningcrux.com/logo-dark.png',
        'intro': "Download free udemy+skillshare+individual+and more courses free of costs",
        'type': "Downoload + watch online ",
        'name': 'Learning crux (illegal)',
        'url': 'https://www.learningcrux.com/',
    }
    ,
    {
        'id': 0,
        'image': 'https://tutflix.com/wp-content/uploads/2020/06/Copy-of-Tutorials-Netflix-4.png',
        'intro': "Download free udemy+skillshare+individual+and more courses free of costs",
        'type': "Downoload + watch online ",
        'name': 'Learning crux (illegal)',
        'url': 'https://tutflix.com/',
    }
     ]
},
{
    'name':'free_softwares_illegal',
     'image': 'https://brutalbusiness.com/wp-content/uploads/2015/12/07/GetintroPC.png',
    'intro': "Download free udemy+skillshare+individual+and more courses free of costs",
'start' : [
    
        {
            'id': 0,
            'image': 'https://brutalbusiness.com/wp-content/uploads/2015/12/07/GetintroPC.png',
            'intro': "Download Free Your Desired App",
            'type': "download softwares desired for your niche",
            'name': 'get intro pc (illegal)',
            'url': 'https://tutflix.com/',
        },
    ]
},
{
    'name':'free_books_illegal',
     'image': 'https://www.pdfdrive.com/assets/img/logo-1.png.pagespeed.ce.vTZcG00TGG.png',
    'intro': "Download free udemy+skillshare+individual+and more courses free of costs",
    'start' :[
    {
        'id': 0,
        'image': 'https://librarygenesis.pro/wp-content/uploads/2020/07/library_genesis-1200x675.png',
        'intro': "Download free books",
        'type': "download any book",
        'name': 'library genisis (illegal)',
        'url': 'http://libgen.li/',
    },
    {
        'id': 0,
        'image': 'https://www.pdfdrive.com/assets/img/logo-1.png.pagespeed.ce.vTZcG00TGG.png',
        'intro': "Download free books",
        'type': "Downlad any book",
        'name': 'pdf drive (illegal)',
        'url': 'https://www.pdfdrive.com/',
    }
    ,
    {
        'id': 0,
        'image': 'https://miro.medium.com/max/1200/1*UbVgZ1J254k2E7NSsEAL9g.jpeg',
        'intro': "Download free books",
        'type': "free books and science papers",
        'name': 'sci hub (illegal)',
        'url': 'https://scihub.wikicn.top/',
    }
  ]
}
]




youTube_channnels = [
  
    {
        "id": "1",
        'image': "https://www.technotification.com/wp-content/uploads/2017/06/Best-youtube-channels-to-learn-coding.jpg",
        'type':'Youtube videos',"name" : "A Little of Everything (Web Dev, Computer Science, and Musings)",

        "start": [
            
            {
                'type':'Youtube videos',"name": "Tom Scott:",
                "intro":"A science and tech focused vlog, with a general focus on computer science topics (given that the host is/was a computer programmer).",
                "url": "https://www.youtube.com/user/enyay",
                'id': 'UCBa659QWEk1AI4Tg--mrJ2A'
            },
            {
                'id': 'UCXgGY0wkgOzynnHvSEVmE3A',
                "url": "https://www.youtube.com/user/hiteshitube",
                'type':'Youtube videos',"name": "Hitesh Choudhary",
                "intro": "An informative young man educates the user when it comes to programming languages as well as information security, along with the occasional vlog"
            },
            {
                'id': 'UCeVMnSShP_Iviwkknt83cww',
                "url": "https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww",
                'type':'Youtube videos',"name": "Code With Harry",
                "intro": "Code With Harry is an attempt to teach basics and those coding techniques to people in short time which took him ages to learn (Mostly Hindi Tutorials). At Code With Harry, he provide a quick and to the point demo along with resources of anything and everything he teach. Source code and other resources are hosted on his website CodeWithHarry.com."
            },
            {
                'id': 'UCeVMnSShP_Iviwkknt83cww',
                "url": "https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww",
                'type':'Youtube videos',"name": "CS Dojo",
                "intro": "All type of fun content and also he left Google."
            },
            {
                'id': 'UC4JX40jDee_tINbkjycV4Sg',
                "url": "https://www.youtube.com/c/TechWithTim/featured",
                'type':'Youtube videos',"name": "Tech With Tim",
                "intro": "Python Programming, Game Development, Pygame, Java Tutorials and Machine Learning. This is a list of a few of the things I love to post on my channel. My goal is share my knowledge of programming with you and allow everyone access to education for FREE."
            },
            {
                'id': 'UC8g_o_0wHJUsp67lJA69yhg',
                "url": "https://www.youtube.com/channel/UC8g_o_0wHJUsp67lJA69yhg",
                'type':'Youtube videos',"name": "Joe Parys Academy",
                "intro": "Joe Parys’s channel features free content from his own website and Udemy, including, but not limited to, tutorials for various programming languages, cryptocurrency, growing an online business, videography, and Final Cut Pro X (A macOSe-exclusive video-editing software"
            },
            {
                'id': 'UCyU5wkjgQYGRB0hIHMwm2Sg',
                "url": "https://www.youtube.com/user/LevelUpTuts",
                'type':'Youtube videos',"name": "LevelUpTuts",
                "intro": "Scott Tolinski – producer and maintainer of the channel, friends with the people behind LearnCode.academy, Josh Owens’ Space Dojo, DevTips, and Wes Bos - aims to offer current, accessible, in-depth, high-quality content on all things web development and design with over 840+ video tutorials and counting."
            },
            {
                'id': 'UCzyuZJ8zZ-Lhfnz41DG5qLw',
                "url": "https://www.youtube.com/user/TheCharmefis/featured",
                'type':'Youtube videos',"name": "mmtuts",
                "intro": "mmtuts (a.k.a MultiMedia Tutorials) aims to provide tutorials spanning the gamut of programming, video editing/production, animation, and graphic design."
            },
            
            {
                'id': 'UCvjgXvBlbQiydffZU7m1_aw',
                "url": "https://www.youtube.com/user/shiffman",
                'type':'Youtube videos',"name": "The Coding Train",
                "intro": "A seeming Jack of All Trades, Daniel Shiffman walks you through a wide range of topics like p5.js (JS, HTML, CSS), Neural Networks and Machine Learning, The Nature of Code (Simulating Natural Systems with Processing), etc. He seems to have a nice grasp on Full-Stack development and computer science."
            },
            {
                'id': 'UCJbPGzawDH1njbqV-D5HqKw',
                "url": "https://www.youtube.com/user/thenewboston",
                'type':'Youtube videos',"name": "Thenewboston",
                "intro": "Bucky Roberts’ immensely popular channel features over 4,200 video tutorials, diving through the vast expanses known as programming, web design, game development, graphic design, and networking. For those interested, he also delves intro other asides like the sciences (biology, math, physics) and DIY projects (how to build a computer, Go Kart, Beer, etc.)"
            },
            {
                'id': 'UC29ju8bIPH5as8OGnQzwJyA',
                "url": "https://www.youtube.com/user/TechGuyWeb",
                'type':'Youtube videos',"name": "Traversy Media",
                "intro": "Brad Traversy, the man behind this channel/company, explores Full-Stack web development with his current tutorials on all things JavaScript (React, Redux, Node, Express, Vue, Angular, Gatsby), Python (Django), Ruby (Rails), Apollo, GraphQL, Docker, and more. He also features a Developer Discussion where he talks about the ‘soft’ side of programming, namely, dealing with your emotions, psychology, and motivation."
            },
            {
                'id': 'UCrqAGUPPMOdo0jfQ6grikZ',
                "url": "https://www.youtube.com/channel/UCrqAGUPPMOdo0jfQ6grikZw",
                'type':'Youtube videos',"name": "Colt Steele",
                "intro": "Colt is a developer with a serious love for teaching. Colt spent a few years teaching people to program at 2 different immersive bootcamps where he helped hundreds of people become web developers and changed their lives. His graduates work at companies like Google, Salesforce, and Square. In 2016 Colt launched his Web Developer Bootcamp course, which has since gone on to become one of the best selling and top rated courses on Udemy. He was also voted Udemy’s Best New Instructor of 2016."
            },
            {
                'id': 'UC54NcJvLCvM2CNaBjd5j6HA',
                "url": "https://www.youtube.com/realtoughcandy",
                'type':'Youtube videos',"name": "Real Tough Candy",
                "intro": "Real Tough Candy combines technical expertise with soft skills in this vlog oriented channel. Besides discussing the latest technologies and trends, RTC offers an insight intro her career, delving intro topics such as freelancing, work ethics, and a lot of tips for beginners. There is a video for everyone in her vast catalog."
            }
            ,
            {
                'id': 'UCSJbGtTlrDami-tDGPUV9-w',
                "url": "https://www.youtube.com/channel/UCSJbGtTlrDami-tDGPUV9-w",
                'type':'Youtube videos',"name": "Ben Ward",
                "intro": " Ben is a software developer who makes videos about React, React Native, GraphQL, Typescript, Node.js, PostgreSQL, Python, and all things coding."
            }
            ,
            {
                'id': 'UC9JWnvl5ZjZv09F5RqiLptw',
                "url": "https://www.youtube.com/ScalerAcademy",
                'type':'Youtube videos',"name": "Scaler Academy",
                "intro": "Accelerate Your Tech Career. Learn computer programming concepts, Data Sturcutres & Algorithms from Ex-Google, Ex-Facebook instructors. Also, watch tech talks from tech leaders, live coding sessions & more."
            }
            ,
            {
                'id': 'UCLNgu_OupwoeESgtab33CCw',
                "url": "https://www.youtube.com/channel/UCLNgu_OupwoeESgtab33CCw",
                'type':'Youtube videos',"name": "Coding Garden with CJ",
                "intro": "CJ does live streams about full stack web development showcasing a wide variety of frameworks and technologies. In the streams, he shows step by step how to use those tools in creating projects. He also has tutorials about topics related to web development."
            }
            ,
         
            {
                'id': 'UCCezIgC97PvUuR4_gbFUs5g',
                "url": "https://www.youtube.com/c/Coreyms",
                'type':'Youtube videos',"name": "Codevolution",
                "intro": "Mostly does React tutorial. High quality content (English)"
            },

        ]
    },
    {
        "id": "2",
        'image': 'https://i.pinimg.com/originals/87/97/77/879777f0a9b857873992612a2427f814.png',
        'type':'Youtube videos',"name": "Computer science",
        "start": [
            {
                'id': 'UC9-y-6csu5WGm29I7JiwpnA',
                "url": "https://www.youtube.com/user/Computerphile",
                'type':'Youtube videos',"name": "Computerphile",
                "intro": "A channel that focuses on more abstract/theoretical topics in computer science. Is less of a tutorial channel and more for those with an interest in theory, etc."
            },
            {
                'id': 'UCX6b17PVsYBQ0ip5gyeme-Q',
                "url": "https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo",
                'type':'Youtube videos',"name": "Crash Course Computer Science",
                "intro": "A very thorough and upbeat channel covering everything within the computer science world: from it’s history to the design decisions that went intro computers, how operating systems work (or don’t work), how the internet works, how our smartphones are getting smarter, and the more mysterious subjects, like quantum computing or the present-day hacking. It also discusses algorithms and data structures, cryptography and cyber security, machine learning, and the singularity. Well-worth the lookup."
            },
            {
                'id': 'UCcabW7890RKJzL968QWEykA',
                "url": "https://www.youtube.com/user/cs50tv/",
                'type':'Youtube videos',"name": "CS50",
                "intro": "Welcome to Harvard University’s Intro to the fundamentals of computer science and the art of programming, taught with languages such as Scratch, C, and Python."
            },
            {
                'id': 'UC0RhatS1pyxInC00YKjjBqQ',
                "url": "https://www.youtube.com/channel/UC0RhatS1pyxInC00YKjjBqQ",
                'type':'Youtube videos',"name": "GeeksforGeeks",
                "intro": "GeeksforGeeks is one of the largest portal for computer science students and professional housing nearly every concept in great detail in data structure, algorithms, operating systems, languages like C++, Java etc. Check out the website GeekforGeeks"
            },
            {
                'id': 'UCxX9wt5FWQUAAz4UrysqK9A',
                "url": "https://www.youtube.com/channel/UCxX9wt5FWQUAAz4UrysqK9A",
                'type':'Youtube videos',"name": "CS Dojo",
                "intro": "CS Dojo is a channel with mostly programming and computer science videos. CS Dojo"
            },
            {
                'id': 'UCWN3xxRkmTPmbKwht9FuE5A',
                "url": "https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A",
                'type':'Youtube videos',"name": "Siraj Raval",
                "intro": "Siraj Raval is on a mission of data literacy. Artificial Intelligence, Mathematics, Science, Technology, he simplfies these topics to help you understand how they work. Using his knowledge you can build wealth and live a happier, more meaningful life. He is the part of the fastest growing AI community in the world! He is also a Data Scientist, AI Educator, Rapper, Author, Speaker, and Founder of the School of AI."
            },
            {
                'id': 'UCLSSymhN34xcMkihq_ULeCQ',
                "url": "https://www.youtube.com/c/AniaKub%C3%B3w",
                'type':'Youtube videos',"name": "Code with Ania Kubów #JavaScriptGames",
                "intro": "Learn JavaScript, React, Html, CSS and Express by making retro game in these tutorials."
            },
        ]
    },
    {
        "id": "3",
        'image': 'https://charisintelligence.com.ng/wp-content/uploads/2020/01/learn-web-development-1024x565.jpg',
        'type':'Youtube videos',"name": "Web Development",
        "start": [
            {
                'id': 'UCMXPX2dNVZUIArP7r8PCO4Q',
                "url": "https://www.youtube.com/channel/UCMXPX2dNVZUIArP7r8PCO4Q",
                'type':'Youtube videos',"name": "BEAM Channel",
                "intro": "Follow Zachary Kessin as he shows you how to build powerful web applications using Elixir, a general-purpose programming language, and BEAM, an Erlang virtual machine (Erlang is also a general-purpose programming language)."
            },
            {
                'id': 'UCwRXb5dUK4cvsHbx-rGzSgw',
                "url": "https://www.youtube.com/user/derekbanas",
                'type':'Youtube videos',"name": "Derek Banas",
                "intro": "(Mostly) A beginner programmer-oriented channel that teaches users the basics or fundamentals of programming languages (C++, JS, Python, etc.)"
            },
            {
                'id': 'UC5Wi_NYysX-LfcqT3Hq9Faw',
                "url": "https://www.youtube.com/user/pizzapokerguy87",
                'type':'Youtube videos',"name": "Dylan Israel",
                "intro": "Tutorials + career/industry advice."
            },
            {
                'id': 'UCkw4JCwteGrDHIsyIIKo4tQ',
                "url": "https://www.youtube.com/user/edurekaIN",
                'type':'Youtube videos',"name": "Edureka",
                "intro": "Features high-quality tutorials and lectures (available also in Hindi and Telugu) where they curate the following topics:,Big Data and Hadoop,DevOps,Block Chain,Artificial Intelligence (AI),Angular,Python,AWS,Data Science and Digital Marketing"
            },
            {
'id': 'UCP-ijZJqrGr0drSrps-Loow',
                "url": "https://www.youtube.com/channel/UCP-ijZJqrGr0drSrps-Loow",
                'type':'Youtube videos',"name": "Logictuts",
                "intro": "Featuring web development tutorials in the Hindi language."
            },
        ]
    },
    {
        "id": "2",
        'image': 'https://www.delta-solutions.nl/wp-content/uploads/2019/10/full-stack-development-by-weblineindia.jpg',
        'type':'Youtube videos',"name": "Full stack",
        "start": [
            {
                'id': 'UCVTlvUkGslCV_h-nSAId8Sw',
                "url": "https://www.youtube.com/user/learncodeacademy",
                "intro": "Free, current web development tutorials covering the entire development stack (Front-End, Back-End, DevOps, Server Administration, and Deployment Stategies).",
                'type':'Youtube videos',"name": "LearnCode.academy"
            },
            {
                'id': 'UCwHrYi0GL6dmYaRB0StEbEA',
                "url": "https://www.youtube.com/user/CodersGuide",
                'type':'Youtube videos',"name": "Neil Rowe",
                "intro": "This channel features more Front-End tutorials (think HTML, CSS, JS, and Bootstrap) than Back-End (Java, building a Windows web server with IIS, PHP, and MySQL)."
            },
            {
                'id': 'UCW5YeuERMmlnqo4oq8vwUpg',
                "url": "https://www.youtube.com/channel/UCW5YeuERMmlnqo4oq8vwUpg",
                'type':'Youtube videos',"name": "The Net Ninja",
                "intro": "Inspired by the Martial Arts, Shaun focuses on getting you towards ‘black-belt’ mastery with his deep-dive intro Full-Stack web development tutorials, featuring JavaScript (ES6, React & Redux, Vue, Angular, Node), Python (Django), GraphQL, MongoDB, Git & GitHub, HTML5, CSS3, and more."
            },
            {
                'id': 'UCWv7vMbMWH4-V0ZXdmDpPBA',
                "url": "https://www.youtube.com/user/programmingwithmosh",
                'type':'Youtube videos',"name": "Programming with Mosh",
                "intro": " Code along with Mosh Hamedani – a software engineer with 18 years of experience – in his fun, upbeat, no-fluff video tutorials (free on YouTube, paid on his website codewithmosh) where he explores the fundamental tools needed to become a Full-Stack developer (JavaScript, Node, Angular, React, Redux, Python, C#, ASP.NET, Object-Oriented programming)"
            },
            {
                'id': 'UCs6nmQViDpUw0nuIx9c_WvA',
                "url": "https://www.youtube.com/user/ProgrammingKnowledge",
                'type':'Youtube videos',"name": "ProgrammingKnowledge",
                "intro": "This channel covers a huge breadth of languages and frameworks in the context of Full-Stack development, like Git and Github, Bootstrap, Python, JavaScript, Node, Redis, Java, C#, MongoDB, MySQL, Android, ASP.NET, and many more!"
            },
            {
                'id': 'UCFbNIlppjAuEX4znoulh0Cw',
                "url": "https://www.youtube.com/channel/UCFbNIlppjAuEX4znoulh0Cw/",
                'type':'Youtube videos',"name": "Web Dev Simplified",
                "intro": "Kyle Cook’s channel is full of videos about the most useful tools in modern web development, from HTML and CSS to database structure and even AI development for web pages; but it focuses heavily on Javascript and all the tools related with it: NodeJS, React, Express, MongoDB, the recent Deno and many more."
            },
            {
                'id': 'UClb90NQQcskPUGDIXsQEz5Q',
                "url": "https://www.youtube.com/channel/UClb90NQQcskPUGDIXsQEz5Q",
                'type':'Youtube videos',"name": "Dev Ed",
                "intro": "Learn web development, web design, 3d modelling, tools like figma and more without getting bored! The goes of this channel is to get you to become as creative you can be! So if you like to create video games in Unity or develop an application in node.js, stick around and have fun!"

            },
            {
                'id': 'UCqrILQNl5Ed9Dz6CGMyvMTQ',
                "url": "https://www.youtube.com/channel/UCqrILQNl5Ed9Dz6CGMyvMTQ",
                'type':'Youtube videos',"name": "Clever Programmer",
                "intro": "These guys teach Full-Stack Web Development through a Project based approach."
            },
           
        ]
    },
    {
        "id": "2",
        'image': 'https://i.ytimg.com/vi/f6FJTWZgoQ0/hqdefault.jpg',
        'type':'Youtube videos',"name": "Front-End/Design",
        "start": [
            {
                'id': 'UCVyRiMvfUNMA1UPlDPzG5Ow',
                "url": "https://www.youtube.com/channel/UCVyRiMvfUNMA1UPlDPzG5Ow",
                'type':'Youtube videos',"name": "DesignCourse",
                "intro": "Here you can learn more about making good looking websites via Graphic Design and Front-End Development. This channel also features Full-Stack Development tutorials."
            },
            {
            'id': 'UCyIe-61Y8C4_o-zZCtO4ETQ',
                "url": "https://www.youtube.com/user/DevTipsForDesigners",
                'type':'Youtube videos',"name": "DevTips",
                "intro": "The sister-channel of Fun Fun Function, this fun (and funny) design-oriented channel features tutorials and tips/opinions on all things design/front-end related like CSS, JavaScript, React, Adobe XD, and container platforms (think Docker and Kubernetes)."
            },
            {
                'id': ' UCoebwHSTvwalADTJhps0emA',
                "url": "https://www.youtube.com/channel/UCbwXnUipZsLfUckBPsC7Jog",
                'type':'Youtube videos',"name": "Online Tutorials",
                "intro": "Online Tutorials and its sister channel, Creative Creations, is rich with beautiful, modular snippets of HTML5 and CSS3 design tutorials."
            },
            {
                'id': '',
                "url": "https://www.youtube.com/user/wesbos",
                'type':'Youtube videos',"name": "Wes Bos",
                "intro": "Follow Wes Bos as he teaches you all about Wordpress, JavaScript, CSS3, and HTML5 in his web development tutorials, his javascript30 course in which he builds 30 different projects everyday, is very popular and is recommended by many famous developers on twitter."
            },
            {
                'id': 'UCJZv4d5rbIKd4QHMPkcABCw',
                "url": "https://www.youtube.com/user/KepowOb/featured",
                'type':'Youtube videos',"name": "Kevin Powell",
                "intro": "With a new video every Wednesday, I’ll be bringing you How Tos and Tutorials, and well as simple tips and tricks. I’m mostly looking to help people who are new to the world of web development."
            },
            {
                'id': 'UC7TizprGknbDalbHplROtag',
                "url": "https://www.youtube.com/channel/UC7TizprGknbDalbHplROtag/featured",
                'type':'Youtube videos',"name": "Layout Land",
                "intro": "Hosted by Jen Simmons. Learn what’s now possible in graphic design on the web — layout, CSS Grid, and more. A series for designers and web developers."
            },
            {
                'id': 'UCD3KVjbb7aq2OiOffuungzw',
                "url": "https://www.youtube.com/channel/UCD3KVjbb7aq2OiOffuungzw",
                'type':'Youtube videos',"name": "DarkCode",
                "intro": "DarkCode is a channel for Learning Web Designs, Websites Building, Ui Designs Using Only HTML5 And CSS3 and some Javascript. If you love creative designs and amazing animations, please do follow him."
            },
            {
                'id': 'UC80PWRj_ZU8Zu0HSMNVwKWw',
                "url": "https://www.youtube.com/channel/UC80PWRj_ZU8Zu0HSMNVwKWw",
                'type':'Youtube videos',"name": "Codevolution",
                "intro": "Codevolution is a channel for learning front end web development.The React series on this channel is one of the best react tutorials out there.It also has tutorials on Angular, ES6 and basic HTML & CSS please do follow him."

        
            },
        ]
    },
    {
        "id": "2",
    'image': 'https://images.idgesg.net/images/article/2020/03/jw_pt4_data_structure_algorithms_java_coding_programmer_2400x1600_pmdumuid_cc0_davidgoh_akindo_gettyimages_531237630_473456596-100834803-large.jpg',
        'type':'Youtube videos',"name": "Data Structures and Algorithms",
        "start": [
            {
                'id': 'UClEEsT7DkdVO_fkrBw0OTrA',
                "url": "https://www.youtube.com/user/mycodeschool",
                'type':'Youtube videos',"name": "mycodeschool",
                "intro": "MyCodeSchool is a channel for Learning Data structures, Programming Interview Questions, Algorithms, Recursion, Time Complexity Analysis, Mathematics for Programmers and pointers in c/c++."
            },
            {
                'id': 'UCF7BExjT2zH_mmyqOB139Dg',
                "url": "https://www.youtube.com/playlist?list=PLKKfKV1b9e8ps6dD3QA5KFfHdiWj9cB1s",
                'type':'Youtube videos',"name": "Apni Kaksha",
                "intro": "Apni kaksha is a channel for Learning Data structures, Programming Interview Questions, Algorithms, Recursion, Time Complexity Analysis, Mathematics for Programmers and pointers in c/c++ and all interview related stuffs"
            },
          
            {
                'id': 'UC-yuWVUplUJZvieEligKBkA',
                "url": "https://www.youtube.com/playlist?list=PLVlQHNRLflP_OxF1QJoGBwH_TnZszHR_j",
                'type':'Youtube videos',"name": "Naresh i Technologies",
                "intro": "Naresh i Technologies is a channel to learn various programming languages and these video tutorials are used to learn and to be good at all the Data Structure Algorithms with their implementations in C programming language in a very clear manner."
            },
            {
                'id': 'UCM-yUTYGmrNvKOCcAl21g3w',
                "url": "https://www.youtube.com/channel/UCM-yUTYGmrNvKOCcAl21g3w",
                'type':'Youtube videos',"name": "Jenny’s lectures CS/IT NET&JRF",
                "intro": "Jenny’s Lectures CS/IT NET&JRF is a Free YouTube Channel providing Computer Science / Information Technology / Computer-related tutorials including Important Computer Science Tutorials and much more. Their Data Structure and Algorithms playlist is outstanding. It is covered using C Language. The explanation is in such a manner that any newbie can easily grasp the concepts"
            },
            {
                'id': 'UCvLEP7Hu6SHd5a2CWeQXalg',
                "url": "https://www.youtube.com/channel/UCvLEP7Hu6SHd5a2CWeQXalg/videos",
                'type':'Youtube videos',"name": "Inside Code",
                "intro": "Inside Code creates content about Data Structures and Algorithms in Python programming language."

        
    },
        ]
    },
    {
        "id": "2",
        'image': 'https://cdn.datafloq.com/cache/blog_images/1200x630/best-gitter-channels-data-science-machine-learning.jpg',
        'type':'Youtube videos',"name": "Machine Learning and Data Science",
        "start": [
            {
                'id': 'UCYO_jab_esuFRV4b17AJtAw"',
                "url": "https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw",
                'type':'Youtube videos',"name": "3Blue1Brown",
                "intro": "3blue1brown, by Grant Sanderson, is some combination of math and entertainment, depending on your disposition. The goal is for explanations to be driven by animations and for difficult problems to be made simple with changes in perspective(this channel has very good explaination about deep nural Network and CNN)"
            },
            {
                'id': 'UCV8e2g4IWQqK71bbzGDEI4Q',
                "url": "https://www.youtube.com/channel/UCV8e2g4IWQqK71bbzGDEI4Q",
                'type':'Youtube videos',"name": "Data Professor",
                "intro": "This channel provides Data Science contents consisting of explainer videos and practical tutorials by Chanin Nantasenamat, Ph.D"
            },
        ]
    },
    {
        "id": "2",
        'image': 'https://i.ytimg.com/vi/pQtdCAeHUgA/maxresdefault.jpg',
        'type':'Youtube videos',"name": "Game Development",
        "start": [
            {
                'id': 'UC-yuWVUplUJZvieEligKBkA',
                "url": "https://www.youtube.com/channel/UCQ-W1KE9EYfdxhL6S4twUNw",
                'type':'Youtube videos',"name": "The Cherno",
                "intro": "Focuses mainly on Game Development and related topics like C++ and Git."
            },
            {
                'id': 'UC-yuWVUplUJZvieEligKBkA',
                "url": "https://www.youtube.com/channel/UC-yuWVUplUJZvieEligKBkA",
                'type':'Youtube videos',"name": "javidx9",
                "intro": "Talks about implementations of C++ in Game Development, Networking and many more."
            },
                {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://i.redd.it/3481o2vr12851.jpg',
        'intro': 'The man behind the loading screen of the latest blender(2.9), he is popular for his one minute tutorials which are for intermediate to advanced blender users',
        'name': 'Ian Hubert',
        'url': 'https://www.youtube.com/user/mrdodobird'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://www.blendernation.com/wp-content/uploads/2019/11/image4-1.jpg',
        'intro': 'Tutorials on animations,visual effects and Blender.',
        'name': 'CG Geek',
        'url': 'https://www.youtube.com/user/Blenderfan93'
    },
     {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://cdnb.artstation.com/p/assets/images/images/014/366/439/large/nicholas-zaris-blenderft.jpg',
        'intro': 'Best for learning Blender which is used for making 3D models.',
        'name': 'Blender Guru',
        'url': 'https://www.youtube.com/playlist?list=PLjEaoINr3zgEq0u2MzVgAaHEBt--xLB6U'
    },
     {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/9/90/Tim_Schafer_and_2PP_at_PAX_Prime_2012.jpg',
        'intro': 'Documentaries of the game industry, get inspired.',
        'name': '2PlayerProductions',
        'url': 'https://www.youtube.com/user/2PlayerProductions'
    },
     {
        'id': 'UCd_lJ4zSp9wZDNyeKCWUstg',
        'type': 'Youtube',
        'image': 'https://www.askgamedev.com/wp-content/uploads/2021/01/EP101-small.png',
        'intro': 'All about Game industry,facts and tips to get into it.',
        'name': 'Ask Gamedev',
        'url': 'https://www.youtube.com/channel/UCd_lJ4zSp9wZDNyeKCWUstg'
    },
     {
        'id': 'UCJklo0Zl5tLV9kkk_Jd81EA',
        'type': 'Youtube',
        'image': 'https://mir-s3-cdn-cf.behance.net/projects/404/3cf83946741035.Y3JvcCwxMjAyLDk0MSwwLDEzMA.jpg',
        'intro': 'All about the design,dedicated especilly to the character design',
        'name': 'Brookes Eggleston',
        'url': 'https://www.youtube.com/channel/UCJklo0Zl5tLV9kkk_Jd81EA'
    },
    {
        'id': 'UCKCTmact-90hXpV2ns8GSsA',
        'type': 'Youtube',
        'image': 'https://devducks.com/static/devducks/imgs/devducks-by-devrant2.jpg',
        'intro': 'A channel for organizing your projects and planning it.',
        'name': 'Dev Duck',
        'url': 'https://www.youtube.com/channel/UCKCTmact-90hXpV2ns8GSsA'
    },
    {
        'id': 'UCH1svLGqmyVuCnHCHDr0EXw',
        'type': 'Youtube',
        'image': 'https://filmstorm.net/content/images/2020/08/smallLogoDark-1-1.png',
        'intro': 'Intermediate to Advanced tutorials.',
        'name': 'Filmstorm',
        'url': 'https://www.youtube.com/channel/UCH1svLGqmyVuCnHCHDr0EXw'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://m.media-amazon.com/images/I/51GqvROndpL.jpg',
        'intro': 'Get to know how to plan your big projects,more about system design of games.',
        'name': 'Adam Millard',
        'url': 'https://www.youtube.com/user/Thefearalcarrot'
    },
    {
        'id': 'UCLyVUwlB_Hahir_VsKkGPIA',
        'type': 'Youtube',
        'image': 'https://i.ytimg.com/vi/h0LJg1cfGhQ/maxresdefault.jpg',
        'intro': 'A channel which recreates popular scenes and mechanics in games.',
        'name': 'Mix and Jam',
        'url': 'https://www.youtube.com/channel/UCLyVUwlB_Hahir_VsKkGPIA'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://i.ytimg.com/vi/9bbhJi0NBkk/maxresdefault.jpg',
        'intro': 'Game Breakdown and behind the scenes of popular games.',
        'name': 'Game Maker’s Toolkit',
        'url': 'https://www.youtube.com/user/McBacon1337'
    },
    {
        'id': 'UCEklP9iLcpExB8vp_fWQseg',
        'type': 'Youtube',
        'image': 'https://miro.medium.com/max/1127/1*i0stRmT9caODvjotCm1lvg.png',
        'intro': 'Dedicated more towards the design and graphics side.',
        'name': 'Makin’ Stuff Look Good',
        'url': 'https://www.youtube.com/channel/UCEklP9iLcpExB8vp_fWQseg'
    },
    {
        'id': 'UCFK6NCbuCIVzA6Yj1G_ZqCg',
        'type': 'Youtube',
        'image': 'https://www.the74million.org/wp-content/uploads/2019/10/codemonkey-lead.jpg',
        'intro': 'This channel has more of intermediate and advanced tutorials and also good beginner tutorials.',
        'name': 'Code Monkey',
        'url': 'https://www.youtube.com/channel/UCFK6NCbuCIVzA6Yj1G_ZqCg'
    },
    {
        'id': 'UC9Z1XWw1kmnvOOFsj6Bzy2g',
        'type': 'Youtube',
        'image': 'https://i.ytimg.com/vi/F--LFn7ZIKw/maxresdefault.jpg',
        'intro': 'This channel teaches you more of the design part than the coding though it has good coding tutorials',
        'name': 'Blackthornprod:',
        'url': 'https://www.youtube.com/channel/UC9Z1XWw1kmnvOOFsj6Bzy2g'
    },
    {
        'id': 'UCX_b3NNQN5bzExm-22-NVVg',
        'type': 'Youtube',
        'image': 'https://6figuredev.com/wp-content/uploads/2019/02/JasonWeimann.png',
        'intro': 'Learn from the veteran from the gaming industry, recommended for intermediate game developers but he also has beginner friendly tutorials.',
        'name': 'Jason Weimann',
        'url': 'https://www.youtube.com/channel/UCX_b3NNQN5bzExm-22-NVVg'
    },
    {
        'id': 'UCIabPXjvT5BVTxRDPCBBOOQ',
        'type': 'Youtube',
        'image': 'https://danisthings.com/assets/ddcoffee.png',
        'intro': 'This channel teaches you more about project management than tutorials,you keep your projects more organized after watching his videos',
        'name': 'Dani',
        'url': 'https://www.youtube.com/channel/UCIabPXjvT5BVTxRDPCBBOOQ'
    },
     {
        'id': 'UC5c-DuzPdH9iaWYdI0v0uzw',
        'type': 'Youtube',
        'image': 'https://www.awesometuts.com/hosted/images/c2/093920145911e99a0a29c21247f076/1_qKcHOdj97r4LBbqLP-7-kA-_1_.png',
        'intro': 'This channel has more projects from scratch to finish ,if you are stuck in any part of your project you can refer to any part of the videos.',
        'name': 'Awesome Tuts',
        'url': 'https://www.youtube.com/channel/UC5c-DuzPdH9iaWYdI0v0uzw'
    },
    {
        'id': 'UC5c-DuzPdH9iaWYdI0v0uzw',
        'type': 'Youtube',
        'image': 'https://www.awesometuts.com/hosted/images/c2/093920145911e99a0a29c21247f076/1_qKcHOdj97r4LBbqLP-7-kA-_1_.png',
        'intro': 'This channel has more projects from scratch to finish ,if you are stuck in any part of your project you can refer to any part of the videos.',
        'name': 'Awesome Tuts',
        'url': 'https://www.youtube.com/channel/UC5c-DuzPdH9iaWYdI0v0uzw'
    },
        {
        'id': 0,'type': 'Youtube',
        'image': 'http://ksr-ugc.imgix.net/assets/018/258/330/203e0e65214f740f7e8ba8ec15720c02_original.jpg',
        'intro': 'Other than teaching game development, he also tells about the game industry.',
        'name': 'Thomas Brush',
        'url': 'https://www.youtube.com/user/thomasmbrush'
    },
      {
        'id': 0,'type': 'Youtube',
        'image': 'http://ksr-ugc.imgix.net/assets/018/258/330/203e0e65214f740f7e8ba8ec15720c02_original.jpg',
        'intro': 'Other than teaching game development, he also tells about the game industry.',
        'name': 'Thomas Brush',
        'url': 'https://www.youtube.com/user/thomasmbrush'
    },
    {
        'id': 1,'type': 'website',
        'image': 'https://blogs.unity3d.com/wp-content/uploads/2020/09/Goodbye-Brackeys_Blog-header_V1_1280x720.png',
        'intro': ' Best for beginners, where one can learn basic stuff and also this channel as projects which can be the base for many projects.',
        'name': 'Brackeys',
        'url':  'https://www.youtube.com/user/Brackeys'
    },
        ]
    },
    {
        "id": "2",
        'image':'https://www.visualcapitalist.com/wp-content/uploads/2019/10/shareable-2-1000x600.jpg',
        'type':'Youtube videos',"name": "Blockchain and Blockchain development",
        "start": [
            {
            'id': 'UC59K-uG2A5ogwIrHw4bmlEg',
                "url": "https://www.youtube.com/watch?v=UqQMSVfugFA&list=PLsyeobzWxl7oY6tZmnZ5S7yTDxyu4zDW-",
                'type':'Youtube videos',"name": "Telusko",
                "intro": " Telusko is a channel where the speaker, Naveen Reddy, speaks about, and teaches various technologies. In the link to the playlist provided above, one can start learning the basics of Blockchain."
            },
            {
                'id': 'UCY0xL8V6NzzFcwzHCgB8orQ',
                "url": "https://www.youtube.com/channel/UCY0xL8V6NzzFcwzHCgB8orQ",
                'type':'Youtube videos',"name": "DappUniversity ",
                "intro": "Dapp university is for those who are heading towards Blockchain development, that is, the development of Decentralized Applications(Dapps).These are basically websites built over blockchain."
            },
        ]
    },
    {
        "id": "2",
        'image': 'https://cdn.ttgtmedia.com/visuals/searchMidmarketSecurity/threat_management/midmarketsecurity_article_008.jpg',
        'type':'Youtube videos',"name": "Bug Bounties",
        "start": [
            {
                'id': 'UCQN2DsjnYH60SFBIA6IkNwg',
                "url": "https://www.youtube.com/c/STOKfredrik/",
                'type':'Youtube videos',"name": "STÖK",
                "intro": " STÖK is a beginner-friendly channel for those who are looking to get started in bug bounty hunting."
            }
        ]

        
    }
]
# @app.route('/', methods=['GET'])
# def home():
#     return '''<h1>Distant Reading Archive</h1>
# <p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/')
def api_all():
    return jsonify(all_resources)
@app.route('/podcasts')
def api_pod():
    return jsonify(Podcasts)
@app.route('/freecourses')
def api_Freecourses():
    return jsonify(freecourses)

@app.route('/everyydaytools')
def api_ETools():
    return jsonify(everyydaytools)
@app.route('/gamedevelopment')
def api_gameDev():
    return jsonify(game_development)




# @app.route('/programming/tools')
# def api_programming_tools():
#     return jsonify(programmingtools)


# @app.route('/programming/tools')
# def api_programming_tools():
#     return jsonify(programmingtools)

@app.route('/webdevelopment')
def api_webDev():
    return jsonify(web_Development)
@app.route('/webdesigner')
def api_webDesign():
    return jsonify(web_designer)
@app.route('/mustprogrammer')
def api_mustprogrammer():
    return jsonify(mustprogrammer)
@app.route('/androiddevelopment/learning')
def api_android_learnings():
    return jsonify(android_learning)
@app.route('/androiddevelopment/courses')
def api_android_coursess():
    return jsonify(android_cources)
@app.route('/androiddevelopment/tools')
def api_android_resourses():
    return jsonify(android_resources)

@app.route('/Ui_Ux')
def api_UI():
    return jsonify(user_interface)




@app.route('/freesoftware')
def api_freesoftware():
    return jsonify(freesoftware)




@app.route('/youtubechannel')
def api_YT():
    return jsonify(youTube_channnels)
@app.route('/motivation')
def api_motivation():
    return jsonify(motivation)
@app.route('/awesome_websites')
def api_awesome_websites():
    return jsonify(awesome_websites)

@app.route('/Stock')
def api_Stock():
    return jsonify(Stock)


'''
\*//////////////////////////////////////////////////////---------- tools ----------////////////////////////////////*/
'''










webDevelopment_tools = [
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

                    
]




Graphic_deginer_tools = [
        {
        'id': 0,'type':'website',
        'image': 'https://speckyboy.com/wp-content/uploads/2019/02/free-adobe-premier-pro-video-templates-01.jpg',
        'intro': "Video is a great way to build trust with potential clients, showcase your products in use, and add a touch of personality to your brand. But if you want to achieve results with video marketing, you need to make sure your videos stand out from the competition.",
        'sum+up': "Free motion graphic templates",
        'name': 'speckybou',
        'url': 'https://speckyboy.com/free-templates-adobe-premier-pro/',
    },
    {
        'id': 0,'type':'website',
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/ira-design.jpg',
        'intro': "Ira Design is a free and open-source illustration tool developed by Creative Tim that help designers to build their own amazing illustrations using awesome gradients and hand-drawn sketch components.",
        'sum+up': "Free motion graphic templates",
        'name': 'Ira Design ',
        'url': 'https://iradesign.io/?ref=creativetim',
    },
    {
        'id': 0,'type':'website',
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/stubborn-generator-768x576.png',
        'intro': "Stubborn is a generator for customizable illustrations that can help you:",
        'sum+up': "illustration creator",
        'name': 'stburn generator',
        'url': 'https://stubborn.fun/',
    },
    {
        'id': 0,'type':'website',
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/vector-creator-768x480.jpeg',
        'intro': "Vector Illustration Creator is a free tool for creating illustrations with no need for design teamwork.",
        'sum+up': "Illustartion creator",
        'name': 'Vector Illustration Creator',
        'url': 'https://icons8.com/vector-creator',
    },
    {
        'id': 0,'type':'website',
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/unnamed-file-768x363.jpg',
        'intro': "Gravit Designer is a full-featured, vector graphic design solution for designers. The program provides a set of powerful tools that help the user to unleash true creativity in designing beautiful and detailed vector imagery. It is suitable for:",
        'sum+up': "Free motion graphic templates",
        'name': 'Gravit designer',
        'url': 'https://www.designer.io/en/',
    },
    {
        'id': 0,'type':'website',
        'image': 'https://creativetimblog.com/blog/wp-content/uploads/2020/02/smash-768x403.png',
        'intro': "Smash Illustration Is a very nice free illustration constructor that offers more than 250 illustrations ready to help you create unique scenes.",
        'sum+up': "Free motion graphic templates",
        'name': 'Smash Illustration ',
        'url': 'https://usesmash.com/',
    },
]


Machine_learning_tools = [
    {
'id': 1,'type':'website',
'image':'https://content.altexsoft.com/media/2018/05/matplotlib_interface.png',
'intro': 'matplotlib is a Python 2D plotting library. Plotting is a visualization of machine learning data. matplotlib originates from MATLAB: Its developer John D. Hunter emulated plotting commands from Mathworks’ MATLAB software.',
'name': 'matplotli',
'url':'https://matplotlib.org/',
    },
    {
'id': 1,'type':'website',
'image':'https://cdn.softwaretestinghelp.com/wp-content/qa/uploads/2018/10/scikit-learn.png',
'intro': 'Scikit-learn is for machine learning development in python. It provides a library for the Python programming language.',
'name': 'Scikit-learn',
'url':'http://scikit-learn.org/stable/',
    },
    {
'id': 1,'type':'website',
'image':'https://cdn.softwaretestinghelp.com/wp-content/qa/uploads/2018/10/pytorch.png',
'intro': 'PyTorch is a Torch based, Python machine learning library. The torch is a Lua based computing framework, scripting language, and machine learning library. it helps in building neural networks through Autograd Module. It provides a variety of optimization algorithms for building neural networks. PyTorch can be used on cloud platforms. It provides distributed training, various tools, and libraries.',
'name': 'PyTorch',
'url':'https://pytorch.org/',
    },
    {
'id': 1,'type':'website',
'image':'https://i.ytimg.com/vi/yjprpOoH5c8/maxresdefault.jpg',
'intro': 'TensorFlow provides a JavaScript library which helps in machine learning. APIs will help you to build and train the models.',
'name': 'TensorFlow',
'url':'https://www.tensorflow.org/',
    },
    {
'id': 1,'type':'website',
'image':'https://cdn.softwaretestinghelp.com/wp-content/qa/uploads/2018/10/weka.png',
'intro': """These machine learning algorithms help in data mining.

Features:

Data preparation
Classification
Regression
Clustering
Visualization and
Association rules mining.
Pros:

Provides online courses for training.
Easy to understand algorithms.
It is good for students as well.
Cons:

Not much documentation and online support are available""",
'name': 'Weka',
'url':'https://www.cs.waikato.ac.nz/ml/weka/',

    },
    {
'id': 1,'type':'website',
'image':'https://cdn.softwaretestinghelp.com/wp-content/qa/uploads/2018/10/keras.png',
'intro': '''Keras is an API for neural networks. It helps in doing quick research and is written in Python.

Features:

It can be used for easy and fast prototyping.
It supports convolution networks.
It assists recurrent networks.
It supports a combination of two networks.
It can be run on the CPU and GPU.
Pros:

User-friendly
Modular
Extensible
Cons:

In order to use Keras, you must need TensorFlow, Theano, or CNTK.''',
'name': 'Keras.io'  ,
'url':'https://keras.io/',
    },
    {
'id': 1,'type':'website',
'image':'https://cdn.softwaretestinghelp.com/wp-content/qa/uploads/2018/10/shogun.png',
'intro': '''Shogun provides various algorithms and data structures for machine learning. These machine learning libraries are used for research and education.

Features:

It provides support vector machines for regression and classification.
It helps in implementing Hidden Markov models.
It offers support for many languages like – Python, Octave, R, Ruby, Java, Scala, and Lua.
Pros:

It can process large data-sets.
Easy to use.
Provides good customer support.
Offers good features and functionalities.''',
'name': 'Shogun',
'url':'https://www.rotato.xyz/',
    },
    {
'id': 1,'type':'website',
'image':'https://openai.com/content/images/2019/05/openai-cover.png',
'intro': 'A single, unified platform, executing a broad range of use cases & methodologies. Create, test & deploy AI models on your own. Usable & Affordable AI. User-friendly & Intuitive.',
'name': 'openai',
'url':'https://openai.com/',
    },
    {
'id': 1,'type':'website',
'image':'https://venturebeat.com/wp-content/uploads/2019/12/dims-e1575998404106.jpg',
'intro': "Artificial intelligence could be one of humanity's most useful inventions. We research and build safe AI systems that learn how to solve problems and advance",
'name': 'deepmind',
'url':'https://deepmind.com/',
    },
    {
'id': 1,'type':'website',
'image':'https://9to5google.com/wp-content/uploads/sites/4/2018/05/google-ai-logo.jpg',
'intro': 'Researchers across Google are innovating across many domains. We challenge conventions and reimagine technology so that everyone can benefit.',
'name': 'research.google',
'url':'https://research.googleblog.com/',
    },
    

]
gameDevelopment_tools = [
     {
        'id': 1,
'image':'https://www.edureka.co/blog/wp-content/uploads/2019/10/snake-game-in-python.png',
'type':'website',
'intro': 'Beginner friendly tutorials',
'name': 'Snake game for beginners',
'url': 'https://codewithharry.com/videos/python-game-development-1',
    },
     {
        'id': 1,
'image':'https://i.ytimg.com/vi/2MIFlGg5jJ0/maxresdefault.jpg',
'type':'website',
'intro': ' A huge library with ready-made 3D models - a lot are free, usefull not only for blender or in gaming',
'name': 'Free3D',
'url': 'https://free3d.com/',
    },
     {
        'id': 1,
'image':'https://www.blender.org/wp-content/uploads/2019/07/blender_render-1280x720.jpg',
'type':'website',
'intro': ' For 3D art, this is not only used by beginners but also for the AAA level games in the industry.',
'name': 'Blender',
'url': 'https://www.blender.org/',
    },
    {
        'id': 1,
'image':'https://cloud.addictivetips.com/wp-content/uploads/2020/03/single-window-mode-e1585553498794.png',
'type':'website',
'intro': ' For making 2D art.',
'name': 'GIMP',
'url': 'https://gimp.org/',
    },
    {
        'id': 1,
'image':'https://www.awn.com/sites/default/files/styles/large_featured/public/image/featured/1017248-mixamo-fuse-adds-support-kinect-windows-v2.png',
'type':'website',
'intro': ' For Rigging your 3D models and animating them by selecting the templates in it.',
'name': 'Mixamo',
'url': 'https://www.mixamo.com/#/',
    },
    
    {
        'id': 1,
'image':'https://digitalphotovideonews.files.wordpress.com/2014/03/28b68-3dvalley.jpg',
'type':'Stock website',
'intro': 'Welcome to 3Dvalley.com, a place for free 3D models, textures, tutorials and other resources for the CGI artist, since 2003.',
'name': '3dvalley',
'url':'http://www.3dvalley.com/',
    }
]
Ui_Ux_tools = [
    {
'id': 1,
'image':'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5c5957de3e262c46a81b4611_Artboard%2BCopy-p-1600.png',
'intro': 'Slick mockup movies and images for promo videos, presentations, portfolios, app store images.Showcasing like the big boys is no longer just for the big boys.',
'name': 'Rotato',
'url':'https://www.rotato.xyz/',
'type': 'mockups',
'price': 'half free'
    },
    {
'id': 2,
'image': 'https://miro.medium.com/max/1600/1*oxxU6j6GXYODNT2is-KU6Q.gif',
'intro': 'Bring your apps and games to life with real-time animation. Rive is a powerful design and animation tool, which allows designers and developers to easily',
'name': 'rive 2',
'url':'https://www.2dimensions.com/',
'type': 'animation',
'price': 'free'
    },
    {
        'id': 3,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5bf6e0c690b6c76a53804bdc_answers_calculator.png',
'intro': 'Understand how users are really experiencing your site without drowning in numbers Traditional web analytics tools help you analyze traffic data. But numbers alone can’t tell you what users really do on your site — Hotjar will.',
'name': 'hotjar',
'url':'https://www.hotjar.com/?utm_expid=.EinRyQaiRjGYjFEJFTUl4Q.0&utm_referrer=',
'type': 'analytics',
'price': 'paid'
    },
    {
        'id': 4,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5be9b020d015a1f9ec9a5442_banner-2.png',
'intro': 'Are you working with design files? Start saving time today.In all plans you can present, comment, create screen flows, and inspect Sketch, Adobe XD, Photoshop, Illustrator, & Figma files - using our web, macOS, Windows, & Linux app',
'name': 'Avocode',
'url':'https://avocode.com/hand-off-and-inspect',
'type': 'UI/UX designing',
'price': 'paid'
    },
    {
        'id': 5,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5bc453b95a68ee5fe21bc6b4_Screen%20Shot%202018-10-15%20at%2010.45.18%20AM.png',
'intro': 'Are you working with design files? Start saving time today.In all plans you can present, comment, create screen flows, and inspect Sketch, Adobe XD, Photoshop, Illustrator, & Figma files - using our web, macOS, Windows, & Linux app',
'name': 'micro',
'url':'https://realtimeboard.com/',
'type': 'team collaboration for brainstroming + video call',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5ba39a9e805bfa74a4b08ddf_1_F19-hrmAQppP33zh1G2jgQ-p-1600.png',
'intro': 'To empower the work of design teams by facilitating a creative synergy through effortless collaboration.',
'name': 'plant',
'url':'https://plantapp.io/#about',
'type': 'team collaboration for brainstroming + video call',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b866b1515ad26e6cea79353_2017-character_personas.jpg',
'intro': 'Generate professional, customizable buyer persona documents with the help of this quick and intuitive generator.',
'name': 'Make my persona',
'url': 'https://www.hubspot.com/make-my-persona',
'type': 'personal portfolio',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b769ac79183f17ee9fe0942_by%20Norde.png',
'intro': 'Vaadin comes with a big set of web components that are fine-tuned for UX, performance, and accessibility.',
'name': 'vaadin',
'url':'https://vaadin.com/',
'type': 'web apps => java',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b583ac6fc79dd91ac4f68af_30134265966479.5b075bbf1b0a7.jpg',
'intro': 'Discover how real users interact with your prototype: define missions, collect actionable insights and analyze how your design performed, with 0 lines of code.',
'name': 'maze',
'url':'https://maze.design/',
'type': 'ui/ux testing + analytics for prototypes',
'price': 'free 1 month trial'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b3c86048d4e3381013434c0_color-tool-v2-4x3.gif',
'intro': 'The Material Theme Editor helps you make your own branded symbol library and apply global style changes to color, shape, and typography.',
'name': 'gallery',
'url':'https://gallery.io/apps',
'type': 'matrial theme editor',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5afb0c4a5d83d9375a8d19d0_social_tout.png',
'intro': "By choosing a set of 50 colors, you'll train a neural network powered algorithm to generate colors you like and block ones you don’t, right in your browser.",
'name': 'khroma',
'url':'http://khroma.co/',
'type': 'Design with colors you love. Khroma uses AI to learn which colors you like and creates limitless palettes for you to discover, search, and save.',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5ac3825ee45951aaec5936b0_homepage-bg-669c8ea95a9ede671933dffb254f493a23de2d7a039f90bfbbac9ecd09f78225.svg',
'intro': 'Share your ideas visually. Lightning fast.',
'name': 'gallery',
'url':'https://whimsical.co/',
'type': 'brainstrming workspace',
'price': 'create 4 free boards '
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5a5dc7eb3e2b760001e215f4_Illustration%20by%20Iza%20Dudzik.jpg',
'intro': 'Piece hi-fi interactions together, build sensor-aided prototypes and share your amazing creations in a matter of minutes.',
'name': 'protopie',
'url':'https://www.protopie.io/',
'type': 'prototyping tool',
'price': 'free for students'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5a312b470672a700015a499c_brics.gif',
'intro': 'Blocs Website Builder Fast, easy to use and powerful visual web design software, that lets you create responsive websites without writing code.',
'name': 'blocs',
'url':'https://blocsapp.com/',
'type': 'websitebuilder',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9cb80a71c7d00019122e2_lottie.png',
'intro': 'Lottie is an iOS, Android, and React Native library that renders After Effects animations in real time, allowing apps to use animations as easily as they use static images.',
'name': 'lottie',
'url':'https://lottiefiles.com/getting-started#',
'type': 'animation maker',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9c715775aae00019a177c_monotype-library-subscription_lead-image-p-1600.jpeg',
'intro': 'With more than 2,200 font families all in one location, you can easily find the perfect typeface for your project. Whether it’s for your own, a client’s or your company’s design, having complete access to a broad selection of high-quality, premium type is a must.',
'name': 'monotype library',
'url':'https://blocsapp.com/',
'type': 'fonts',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e8a73a90983b000144f01e_webflow.png',
'intro': 'The modern way to build for the web Webflow empowers designers to build professional, custom websites in a completely visual canvas. View dashboard',

'name': 'webflows',
'url':'https://webflow.com/',
'type': 'websitebuilder',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e215007032510001bb636f_home-screenshot.png',
'intro': "Online app that enables designers to customize their own typeface in a few clicks.",
'name': 'prototypo',
'url':'https://www.prototypo.io/',
'type': 'fonts',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e218ae3f6bfa0001113de7_invision-logo.jpg',
'intro': "The world's leading prototyping, collaboration & workflow platform",
'name': 'invision',
'url':'https://www.invisionapp.com/',
'type': 'prototyping + devlopment fro m design',
'price': 'free'
    },
    {
        'id': 6,
'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Adobe_XD_CC_icon.svg/1200px-Adobe_XD_CC_icon.svg.png',
'intro': "Share your story with designs that look and feel like the real thing. Wireframe, animate, prototype, collaborate and more — it’s all right here, all in one place.",
'name': 'Adobe xd',
'url':'https://www.adobe.com/in/products/xd.html',
'type': 'ui/ux designing',
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
        'intro': 'Mix-&-match illustrations of people with a design library',
        'name': 'Hummans',
        'url': 'https://www.humaaans.com/?ref=producthunt',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5bf6e3d14ae3421f52814444_download.jpg',
        'intro': 'Mobbin is a hand-picked collection of the latest mobile design patterns from apps that reflect the best in design. Get inspiration from over 150 iOS apps and 8,000 patterns (screenshots from iPhone X) available on the platform. Sign up to save your favorite patterns.',
        'name': 'mobbin',
        'url': 'https://mobbin.design/',
        'extra': 'ios design pattrens',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59fc7d4b605d4b0001f003e9_marriot_copy.jpg',
        'intro': 'Take responsive screenshots with the click of button',
        'name': 'Responsive screenshorts',
        'url': 'https://responsive-screenshots.com/',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "Resource",
    },
    
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5c05205a90375ebb9d52fad7_Image-p-1600.jpeg',
        'intro': 'Mix-&-match illustrations of people with a design library',
        'name': 'Hummans',
        'url': 'https://www.humaaans.com/?ref=producthunt',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9bea6e87a4d000109dbd1_jakub-dziubak-394720-(1).jpg',
        'intro': 'Beautiful high quality free images and photos you can download and use for any project. No attribution required.',
        'name': 'unsplash',
        'url': 'https://unsplash.com/',
        'extra': 'Photos',
        'price': 'free',
        'type': "Resource",
    },
    
    {
        'id': 0,
        'image': 'https://www.logo-designer.co/wp-content/uploads/2013/09/iStock-logo-design-identity-getty-images-Build.jpg',
        'intro': 'free photos',
        'name': 'istock',
        'url': 'https://www.istockphoto.com/collaboration/boards/L9m43WDlbUO8O94wqUFIIA',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://cdn.joypixels.com/sections/coverphotos/6.0%20Release%20FINAL%20FINAL-02-min.png',
        'intro': 'New for 2020! JoyPixels 6.0 includes 3,342 originally crafted icon designs and is 100% Unicode 13 compatible. We offer the largest selection of files ranging from png, svg, iconjar, sprites, and fonts.',
        'name': 'PIXELS',
        'url': 'https://www.joypixels.com/',
        'extra': 'Emoji',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://static-cdn.pixlr.com/images/pixlr-header-logo.png',
        'intro': 'Pixlr, the World’s Favorite #1 Online Photo Editor lets you edit photos right in your browser for Free. Experience next level, intuitive photo editing with AI-powered tools for quick yet professional edits',
        'name': 'PIXLR',
        'url': 'https://www.joypixels.com/',
        'extra': 'Emoji',
        'price': 'free',
        'type': "Resource",
    },
]

android_tools = [
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








@app.route('/programming/tools')
def api_programming_tools():
    return jsonify(programming_tools)

@app.route('/Ui_Ux/tools')
def api_Ui_Ux_tools():
    return jsonify(Ui_Ux_tools)
@app.route('/gameDevelopment/tools')
def api_gameDevelopment_tools():
    return jsonify(gameDevelopment_tools)
@app.route('/Graphic_deginer/tools')
def api_Graphic_deginer_tools():
    return jsonify(Graphic_deginer_tools)
@app.route('/webDevelopment/tools')
def api_webDevelopment_tools():
    return jsonify(webDevelopment_tools)
@app.route('/android/tools')
def api_android_tools():
    return jsonify(android_tools)
@app.route('/machine_learning/tools')
def api_Machine_learning_tools():
    return jsonify(Machine_learning_tools)




'''
\*//////////////////////////////////////////////////////---------- learning ----------////////////////////////////////*/
'''



Machine_learning_learning = [
    {
                'id':0,
                'image': 'https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/18-06s10.jpg',
                'intro': "This is a basic subject on matrix theory and linear algebra. Emphasis is given to topics that will be useful in other disciplines, including systems of equations, vector spaces, determinants, eigenvalues, similarity, and positive definite matrices.",
                'name': "Introduction to Linear Algebra.",
                'Return': 'Base knowledge',
                'type': 'video + youtube',
                'url':  'https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/'
            },
            {
                'id':0,
                'image': 'https://i.ytimg.com/vi/WUvTyaaNkzM/maxresdefault.jpg',
                'intro': "The goal here is to make calculus feel like something that you yourself could have discovered.",
                'name': "Essence of linear calculus",
                'Return': 'Base knowledge',
                'type': 'video + youtube',
                'url':  'https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr'
            },
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/84251067-b212-4355-a9d3-246d91896b90-41bac59be40f.small.jpg',
                'intro': "Build foundational knowledge of data science with this introduction to probabilistic models, including random processes and the basic elements of statistical inference -- Part of the MITx MicroMasters program in Statistics and Data Science",
                'name': "Probability - The Science of Uncertainty and Datassence of linear algebra",
                'Return': 'knowledge',
                'type': 'video + assigments',
                'url':  'https://www.edx.org/course/introduction-probability-science-mitx-6-041x-2'
            },
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/8e285de1-0242-4e94-8041-84231363caf4-e1a05f019d47.small.jpg',
                'intro': "Learn about the core principles of computer science: algorithmic thinking and computational problem solving.",
                'name': "Algorithm Design and Analysis",
                'Return': 'Base knowledge',
                'type': 'video + assigment',
                'url':  'https://www.edx.org/course/algorithm-design-analysis-pennx-sd3x'
            },
             {
                'id':0,
                'image': 'https://i.ytimg.com/vi/kjBOesZCoqc/maxresdefault.jpg',
                'intro': "A geometric understanding of matrices, determinants, eigen-stuffs and more.",
                'name': "Essence of linear algebra",
                'Return': 'Base knowledge',
                'type': 'video + youtube',
                'url':  'https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab'
            },
             {
                'id':0,
                'image': 'https://blog.udacity.com/wp-content/uploads/2015/11/MLND-blog-post-1024x536.png',
                'intro': "This class will teach you the end-to-end process of investigating data through a machine learning lens. Learn online, with Udacity.",
                'name': "Introduction to Machine Learning Course",
                'Return': 'intermidiate knowledge',
                'type': 'video + assigments',
                'url':  'https://www.udacity.com/course/intro-to-machine-learning--ud120'
            },
            {
                'id':0,
                'image': 'https://blog.udacity.com/wp-content/uploads/2015/11/MLND-blog-post-1024x536.png',
                'intro': "A curated list of practical deep learning and machine learning project ideas",
                'name': "Awesome Deep Learning Project Ideas",
                'Return': 'intermidiate knowledge',
                'type': 'practice',
                'url':  'https://github.com/NirantK/awesome-project-ideas'
            },
            {
                'id':0,
                'image': 'https://i.ytimg.com/vi/kjBOesZCoqc/maxresdefault.jpg',
                'intro': "A geometric understanding of matrices, determinants, eigen-stuffs and more.",
                'name': "Essence of linear algebra",
                'Return': 'Base knowledge',
                'type': 'video + youtube',
                'url':  'https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab'
            },
]
gameDevelopment_learning= [
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://i.redd.it/3481o2vr12851.jpg',
        'intro': 'The man behind the loading screen of the latest blender(2.9), he is popular for his one minute tutorials which are for intermediate to advanced blender users',
        'name': 'Ian Hubert',
        'url': 'https://www.youtube.com/user/mrdodobird'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://www.blendernation.com/wp-content/uploads/2019/11/image4-1.jpg',
        'intro': 'Tutorials on animations,visual effects and Blender.',
        'name': 'CG Geek',
        'url': 'https://www.youtube.com/user/Blenderfan93'
    },
     {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://cdnb.artstation.com/p/assets/images/images/014/366/439/large/nicholas-zaris-blenderft.jpg',
        'intro': 'Best for learning Blender which is used for making 3D models.',
        'name': 'Blender Guru',
        'url': 'https://www.youtube.com/playlist?list=PLjEaoINr3zgEq0u2MzVgAaHEBt--xLB6U'
    },
     {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/9/90/Tim_Schafer_and_2PP_at_PAX_Prime_2012.jpg',
        'intro': 'Documentaries of the game industry, get inspired.',
        'name': '2PlayerProductions',
        'url': 'https://www.youtube.com/user/2PlayerProductions'
    },
     {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://www.askgamedev.com/wp-content/uploads/2021/01/EP101-small.png',
        'intro': 'All about Game industry,facts and tips to get into it.',
        'name': 'Ask Gamedev',
        'url': 'https://www.youtube.com/channel/UCd_lJ4zSp9wZDNyeKCWUstg'
    },
     {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://mir-s3-cdn-cf.behance.net/projects/404/3cf83946741035.Y3JvcCwxMjAyLDk0MSwwLDEzMA.jpg',
        'intro': 'All about the design,dedicated especilly to the character design',
        'name': 'Brookes Eggleston',
        'url': 'https://www.youtube.com/channel/UCJklo0Zl5tLV9kkk_Jd81EA'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://devducks.com/static/devducks/imgs/devducks-by-devrant2.jpg',
        'intro': 'A channel for organizing your projects and planning it.',
        'name': 'Dev Duck',
        'url': 'https://www.youtube.com/channel/UCKCTmact-90hXpV2ns8GSsA'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://filmstorm.net/content/images/2020/08/smallLogoDark-1-1.png',
        'intro': 'Intermediate to Advanced tutorials.',
        'name': 'Filmstorm',
        'url': 'https://www.youtube.com/channel/UCH1svLGqmyVuCnHCHDr0EXw'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://m.media-amazon.com/images/I/51GqvROndpL.jpg',
        'intro': 'Get to know how to plan your big projects,more about system design of games.',
        'name': 'Adam Millard',
        'url': 'https://www.youtube.com/user/Thefearalcarrot'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://i.ytimg.com/vi/h0LJg1cfGhQ/maxresdefault.jpg',
        'intro': 'A channel which recreates popular scenes and mechanics in games.',
        'name': 'Mix and Jam',
        'url': 'https://www.youtube.com/channel/UCLyVUwlB_Hahir_VsKkGPIA'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://i.ytimg.com/vi/9bbhJi0NBkk/maxresdefault.jpg',
        'intro': 'Game Breakdown and behind the scenes of popular games.',
        'name': 'Game Maker’s Toolkit',
        'url': 'https://www.youtube.com/user/McBacon1337'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://miro.medium.com/max/1127/1*i0stRmT9caODvjotCm1lvg.png',
        'intro': 'Dedicated more towards the design and graphics side.',
        'name': 'Makin’ Stuff Look Good',
        'url': 'https://www.youtube.com/channel/UCEklP9iLcpExB8vp_fWQseg'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://www.the74million.org/wp-content/uploads/2019/10/codemonkey-lead.jpg',
        'intro': 'This channel has more of intermediate and advanced tutorials and also good beginner tutorials.',
        'name': 'Code Monkey',
        'url': 'https://www.youtube.com/channel/UCFK6NCbuCIVzA6Yj1G_ZqCg'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://i.ytimg.com/vi/F--LFn7ZIKw/maxresdefault.jpg',
        'intro': 'This channel teaches you more of the design part than the coding though it has good coding tutorials',
        'name': 'Blackthornprod:',
        'url': 'https://www.youtube.com/channel/UC9Z1XWw1kmnvOOFsj6Bzy2g'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://6figuredev.com/wp-content/uploads/2019/02/JasonWeimann.png',
        'intro': 'Learn from the veteran from the gaming industry, recommended for intermediate game developers but he also has beginner friendly tutorials.',
        'name': 'Jason Weimann',
        'url': 'https://www.youtube.com/channel/UCX_b3NNQN5bzExm-22-NVVg'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://danisthings.com/assets/ddcoffee.png',
        'intro': 'This channel teaches you more about project management than tutorials,you keep your projects more organized after watching his videos',
        'name': 'Dani',
        'url': 'https://www.youtube.com/channel/UCIabPXjvT5BVTxRDPCBBOOQ'
    },
     {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://www.awesometuts.com/hosted/images/c2/093920145911e99a0a29c21247f076/1_qKcHOdj97r4LBbqLP-7-kA-_1_.png',
        'intro': 'This channel has more projects from scratch to finish ,if you are stuck in any part of your project you can refer to any part of the videos.',
        'name': 'Awesome Tuts',
        'url': 'https://www.youtube.com/channel/UC5c-DuzPdH9iaWYdI0v0uzw'
    },
    {
        'id': 0,
        'type': 'Youtube',
        'image': 'https://www.awesometuts.com/hosted/images/c2/093920145911e99a0a29c21247f076/1_qKcHOdj97r4LBbqLP-7-kA-_1_.png',
        'intro': 'This channel has more projects from scratch to finish ,if you are stuck in any part of your project you can refer to any part of the videos.',
        'name': 'Awesome Tuts',
        'url': 'https://www.youtube.com/channel/UC5c-DuzPdH9iaWYdI0v0uzw'
    },
        {
        'id': 0,'type': 'Youtube',
        'image': 'http://ksr-ugc.imgix.net/assets/018/258/330/203e0e65214f740f7e8ba8ec15720c02_original.jpg',
        'intro': 'Other than teaching game development, he also tells about the game industry.',
        'name': 'Thomas Brush',
        'url': 'https://www.youtube.com/user/thomasmbrush'
    },
      {
        'id': 0,'type': 'Youtube',
        'image': 'http://ksr-ugc.imgix.net/assets/018/258/330/203e0e65214f740f7e8ba8ec15720c02_original.jpg',
        'intro': 'Other than teaching game development, he also tells about the game industry.',
        'name': 'Thomas Brush',
        'url': 'https://www.youtube.com/user/thomasmbrush'
    },
    {
        'id': 1,'type': 'website',
        'image': 'https://blogs.unity3d.com/wp-content/uploads/2020/09/Goodbye-Brackeys_Blog-header_V1_1280x720.png',
        'intro': ' Best for beginners, where one can learn basic stuff and also this channel as projects which can be the base for many projects.',
        'name': 'Brackeys',
        'url':  'https://www.youtube.com/user/Brackeys'
    },
    {
        'id':2,'type': 'website',
        'image': 'https://cdn2.unrealengine.com/Unreal+Engine%2Fonlinelearning-courses%2FNews_UOLDec_fb_image-1200x630-520419d3e9c82ff29459b6844fb50ed0262e715c.jpg',
        'intro': 'Unreal Online Learning is a free learning platform that offers hands-on video courses and guided learning paths.',
        'name': 'unreal engine',
        'url':  'https://www.unrealengine.com/en-US/onlinelearning-courses'
    },
]
webDevelopment_learning = [
     {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/30kC4o240eHFh0fE6n1PYH/09dbf4e8ca8e19f761a9d754ba4fa50f/image.png',
                'intro': "Classic tower defense game but using CSS to position your towers.",
                'name': "Flexbox Defense",
                'type': 'css Games',
                'url':  'http://www.flexboxdefense.com/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/4tUaHeYUpOP2f5Tv5dTX0F/2ecfc593dae0f7f439501c01e321285b/image.png',
                'intro': "Broswer game to practice identifying HTML selectors for use in CSS stylesheets.",
                'name': "CSS Diner",
                'type': 'css Games',
                'url':  'https://css-diner.netlify.app/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/72nixprDE0M0fwwMkQZbYN/7ce860cb66c6f22eedd8913108d70d2a/image.png',
                'intro': "A browser game where you write CSS code to help you learn CSS grid layout.",
                'name': "Grid Garden",
                'type': 'css Games',
                'url':  'https://cssgridgarden.com/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/58rc7QCmF0ifFvXxUhsi0l/35dcdd264a17a62f830b9584b8d866e1/image.png',
                'intro': "A game for learning CSS flexbox.",
                'name': "Flexbox Froggy",
                'type': 'css Games',
                'url':  'https://flexboxfroggy.com/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/6ngsa311Hwbe2HeUFcVfEf/22a19b83a3f063cdefc9909cb5c4a9c0/banner.png',
                'intro': "CSS code-golfing! Use CSS to replicate targets with smallest possible code",
                'name': "CSSBattle",
                'type': 'css Games',
                'url':  'https://cssbattle.dev/'
            },
]
Ui_Ux_learning = [
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5be9af00cbd406ee1caaff15_expert-advice-unfurl.png',
'intro': "Build your design system like the pros",
'name': 'ui/ux',
'url':'https://www.invisionapp.com/design-system-manager/expert-advice',
'extra': 'ui/ux designing',
'price': 'free',
'type': 'learning+video'
    },
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5b311fa7cbd2eb17d660c209_ui-guide-Designing-search-for%20mobile-apps-p-1600.jpeg',
'intro': "Explore the various ways to implement search and the purpose behind each",
'name': 'ui/ux',
'url':'https://medium.muz.li/designing-search-for-mobile-apps-ab2593e9e413',
'extra': 'ui/ux designing',
'price': 'free',
'type': 'learning+text'
    }
    ,
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5ac380fbf1502e199b611d42_squarepegroundhole_final4.png',
'intro': "I have always believed that Psychology and Design comprise User Experience.",
'name': 'ui/ux',
'url':'https://uxdesign.cc/psychology-design-4-gestalt-principles-to-use-as-your-next-design-solution-fcdec423a6bf',
'extra': 'ui/ux designing',
'price': 'free',
'type': 'learning+text'
    }
    ,
    {
        'id': 6,
'image': 'https://miro.medium.com/max/700/1*3M9hkYLvrJ5xTR2_ZM0FAg.gif',
'intro': "7 Basic Rules for Button Design",
'name': 'ui',
'url':'https://uxplanet.org/7-basic-rules-for-button-design-63dcdf5676b4',
'extra': 'ui/ux designing',
'price': 'free',
'type': 'learning+text'
    }
    ,
    {
        'id': 6,
'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5a68617439ab7c00014d1d3a_170623_dropbox-ecosystem_v01.jpg',
'intro': "Laws of UX is a collection of the maxims and princples that designers can consider when building user interfaces.",
'name': 'ui',
'url':'https://lawsofux.com/',
'extra': 'ui/ux designing',
'price': 'free',
'type': 'learning+text'
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9c297e87a4d000109e13d_1-t2L7WZC7hpZFexm47qzQSA-p-1600.jpeg',
        'intro': 'Collection of articles, videos, and resources made by designers at Facebook.',
        'name': 'facebook design',
        'url': 'http://facebook.design/',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "learning",
    },
    
]
programming_learning =[
    {
        'id': 0,'type': 'website',
        'image': 'https://miro.medium.com/max/1909/1*ywYwvB-aydv0Ovx7K-5P3g.jpeg',
        'intro': "A new take on the age-old question: Should you rewrite your application from scratch, or is that “the single worst strategic mistake that any software company can make”? ",
        'name': 'Lessons from 6 software rewrite stories',
        'url': 'https://medium.com/@herbcaudill/lessons-from-6-software-rewrite-stories-635e4c8f7c22',
        },
    {
        'id': 0,'type': 'website',
        'image': 'https://cdn-media-1.freecodecamp.org/images/1*3pyJUEclXtPt8TNONerTUg.jpeg',
        'intro': "How to escape tutorial purgatory as a new developer — or at any time in your career.",
        'name': 'For a long time I held off from starting my own side projects because of how much I didn’t know how to do.',
        'url': 'https://www.freecodecamp.org/news/how-to-escape-tutorial-purgatory-as-a-new-developer-or-at-any-time-in-your-career-e3a4b2384a40/',
    },
    {
        'id': 0,
        'type': 'website',
        'image': 'https://cdn-media-1.freecodecamp.org/images/1*3pyJUEclXtPt8TNONerTUg.jpeg',
        'intro': "How to escape tutorial purgatory as a new developer — or at any time in your career.",
        'name': 'For a long time I held off from starting my own side projects because of how much I didn’t know how to do.',
        'url': 'https://www.freecodecamp.org/news/how-to-escape-tutorial-purgatory-as-a-new-developer-or-at-any-time-in-your-career-e3a4b2384a40/',
    },
    {
        'id': 0,
        'image': 'https://cdn-media-1.freecodecamp.org/images/1*3pyJUEclXtPt8TNONerTUg.jpeg',
        'type': 'website',
        'intro': "How to escape tutorial purgatory as a new developer — or at any time in your career.",
        'name': 'For a long time I held off from starting my own side projects because of how much I didn’t know how to do.',
        'url': 'https://www.freecodecamp.org/news/how-to-escape-tutorial-purgatory-as-a-new-developer-or-at-any-time-in-your-career-e3a4b2384a40/',
    },
]
android_learning = [
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/8f8e5124-1dab-47e6-8fa6-3fbdc0738f0a-762af069070e.small.jpg',
                'intro': "This course picks up where CS50 leaves off, diving more deeply intro the design and implementation of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap.",
                'name': "CS50's Web Programming with Python and JavaScript",
                'Return': 'free certificate',
                'type': 'video + assigment',
                'url':  'https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript'
            },
            {
                'id':0,
                'image': 'https://abhiandroid-8fb4.kxcdn.com/ui/wp-content/uploads/2018/05/Abhi-Android.png',
                'intro': "website for understanding of andtroid topics",
                'name': "Abhi android",
                'type': 'text',
                'url':  'https://abhiandroid.com/'
            }
            ,
            {
                'id':0,
                'image': 'https://abhiandroid-8fb4.kxcdn.com/ui/wp-content/uploads/2018/05/Abhi-Android.png',
                'intro': "website for understanding of andtroid topics",
                'name': "codelabs for android by google",
                'type': 'text',
                'url':  'https://codelabs.developers.google.com/codelabs'
            },
            {
                'id':0,
                'image': 'https://camo.githubusercontent.com/be3b1262c26ff23b3480c07c4b13ca1d01355a73/68747470733a2f2f692e696d6775722e636f6d2f586778576679462e706e67',
                'intro': "We have Android guides for everyone whether you are a beginner, intermediate or expert. Want to learn how to use the ActionBar or the ins and outs of fragments? We got that. Want to learn about automated unit testing or how to build flexible user interfaces for multiple devices? ",
                'name': "an android guide (github code_path)",
                'type': 'text',
                'url':  'https://github.com/codepath/android_guides/wiki'
            }
        ]





@app.route('/programming/learning')
def api_programming_learning():
    return jsonify(programming_learning)
@app.route('/Ui_Ux/learning')
def api_Ui_Ux_learning():
    return jsonify(Ui_Ux_learning)
@app.route('/gameDevelopment/learning')
def api_gameDevelopment_learning():
    return jsonify(gameDevelopment_learning)
# @learning.route('/Graphic_deginer/learning')
# def api_programming_learning():
#     return jsonify(Graphic_deginer)
@app.route('/webDevelopment/learning')
def api_webDevelopment_learning():
    return jsonify(webDevelopment_learning)
@app.route('/android/learning')
def api_android_learning():
    return jsonify(android_learning)
@app.route('/machine_learning/learning')
def api_machine_learning_learning():
    return jsonify(Machine_learning_learning)






'''
\*//////////////////////////////////////////////////////---------- courses ----------////////////////////////////////*/
'''
 
     

android_courses = [
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/8f8e5124-1dab-47e6-8fa6-3fbdc0738f0a-762af069070e.small.jpg',
                'intro': "This course picks up where CS50 leaves off, diving more deeply intro the design and implementation of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap.",
                'name': "CS50's Web Programming with Python and JavaScript",
                'Return': 'free certificate',
                'type': 'video + assigment',
                'url':  'https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript'
            },
            {
                
                'id':0,
                'image': 'https://developer.android.com/images/kotlin/learn/hero.svg',
                'intro': "Whether you're interested in getting started with Kotlin or are looking to grow your expertise, Google's Kotlin for Android training courses can help you advance your skills.",
                'name': "Learn Kotlin for Android",
                'Return': 'free certificate',
                'type': 'video + text + assigment',
                'url':  'https://developer.android.com/kotlin/campaign/learn'
            
            },
            {
                
                'id':0,
                'image': 'https://developer.android.com/courses/images/android-for-developers.svg',
                'intro': "Whether you're interested in getting started with Kotlin or are looking to grow your expertise, Google's Kotlin for Android training courses can help you advance your skills.",
                'name': " All Android courses provided by google",
                'Return': 'free certificate',
                'type': 'video + text + assigment',
                'url':  'https://developer.android.com/courses'
            
            },
            {
                'id':0,
                'image': 'https://1onjea25cyhx3uvxgs4vu325-wpengine.netdna-ssl.com/wp-content/uploads/2016/06/Develop-for-Android-Chalkboard.jpg',
                'intro': "This course is designed for students who are new to programming, and want to learn how to build Android apps. You don’t need any programming experience to take this course. If you’ve been using a smartphone to surf the web and chat with friends, then you’re our perfect target student!",
                'name': "Android Basics: User Interface",
                'Return': 'certificate',
                'type': 'video +  assigment',
                'url':  'https://www.udacity.com/course/android-basics-nanodegree-by-google--nd803'
            },
            {
                'id':0,
                'image': 'https://s3-us-west-1.amazonaws.com/udacity-content/partner/logo-color-google-1c8cf8f.svg',
                'intro': "Learn to architect and develop Android apps in the Kotlin programming language using industry-proven tools and libraries. With these techniques you'll create apps in less time, writing less code, and with fewer errors.",
                'name': "Developing Android Apps with Kotlin",
                'Return': 'certificate',
                'type': 'video +  assigment',
                'url':  'https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012'
            },
            {
                'id':0,
                'image': 'https://s3-us-west-1.amazonaws.com/udacity-content/partner/logo-color-google-1c8cf8f.svg',
                'intro': "Learn to architect and develop Android apps in the Kotlin programming language using industry-proven tools and libraries. With these techniques you'll create apps in less time, writing less code, and with fewer errors.",
                'name': "Developing Android Apps with Kotlin",
                'Return': 'certificate',
                'type': 'video +  assigment',
                'url':  'https://www.udacity.com/course/developing-android-apps-with-kotlin--ud9012'
            }
            
        ]
webDevelopment_courses = [
    {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/8f8e5124-1dab-47e6-8fa6-3fbdc0738f0a-762af069070e.small.jpg',
                'intro': "This course picks up where CS50 leaves off, diving more deeply intro the design and implementation of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap.",
                'name': "CS50's Web Programming with Python and JavaScript",
                'Return': 'free certificate',
                'type': 'video + assigment',
                'url':  'https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript'
    },
    {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "From the basics to advanced topics with simple, but detailed explanations.",
                'name': "The Modern JavaScript Tutorial",
                'type': 'text',
                'url':  'http://javascript.info/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/4RGBWl2tZ0bYIt0GX7XVw1/25f59ffd9052d12bba2a4f562c2ff25f/image.pnghttps://images.ctfassets.net/aq13lwl6616q/4RGBWl2tZ0bYIt0GX7XVw1/25f59ffd9052d12bba2a4f562c2ff25f/image.png',
                'intro': "Guide for JavaScript & Node.js reliability from A-Z.",
                'name': "Testing JavaScript: Best Practices",
                'type': 'free templates',
                'url':  'https://github.com/goldbergyoni/javascript-testing-best-practices'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "From the basics to advanced topics with simple, but detailed explanations.",
                'name': "The Modern JavaScript Tutorial",
                'type': 'free templates',
                'url':  'http://javascript.info/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png',
                'intro': "From the basics to advanced topics with simple, but detailed explanations.",
                'name': "The Modern JavaScript Tutorial",
                'type': 'free templates',
                'url':  'http://javascript.info/'
            },
            

]

gameDevelopment_courses = [
    {
        'id': 0,
        'image': 'https://files.hubhopper.com/podcast/12514/real-talk-javascript.jpg',
        'intro': 'A sub-reddit for begginers/intermediate game developers where you can ask by sharing videos/links of specific game events, it will really help you in learning game development.',
        'name': 'How Did They Code It',
        'url': 'https://www.reddit.com/r/howdidtheycodeit/'
    },
    {
        'id': 0,
        'image': 'https://d1p8pldpmo4u0v.cloudfront.net/wp-content/uploads/2016/08/Indie_Game_The_Movie_Artwork_1.jpg',
        'intro': ' A facebook group with 120k+ members who help you if your stuck in your project or for networking and get to know about their stories.',
        'name': 'Indie Game Developers',
        'url': 'https://www.facebook.com/groups/IndieGameDevs/about/'
    },
    {
        'id': 0,
        'image': 'https://www.badykov.com/images/2019-04-06-gamedev.jpg',
        'intro': 'A subreddit with 490k+ members ,where you get to know about game development, programming, design, writing, math, art, jams, postmortems and marketing.',
        'name': 'gamedev:',
        'url': 'https://www.reddit.com/r/gamedev/'
    },
  {
        'id': 0,
        'image': 'https://i.ytimg.com/vi/5LhA4Tk_uvI/maxresdefault.jpg',
        'intro': 'Netwokring documentations which are best to learn how to implement multiplayer game features in your project.',
        'name': 'Mirror Networking',
        'url': 'https://mirror-networking.com/docs/'
    },
    {
        'id': 0,
        'image': 'https://cdn.arstechnica.net/wp-content/uploads/2018/02/ARCore-logo.jpg',
        'intro': 'Documentation to implement AR using Unity.',
        'name': 'ARCore',
        'url': 'https://developers.google.com/ar/develop/unity'
    },
     {
        'id': 0,
        'image': 'https://blogs.unity3d.com/wp-content/uploads/2017/09/ML-blog-header-v6.jpg',
        'intro': 'Tutorials on ML agents.',
        'name': 'ML Agents',
        'url': 'https://www.immersivelimit.com/tutorials/unity-ml-agents-tutorial-list'
    },
    {
        'id': 0,
        'image': 'https://hackernoon.com/drafts/1k3j3zqp.png',
        'intro': '10 Reasons Why You Should Learn How To Develop Video Games',
        'name': 'hackernoon article',
        'url': 'https://hackernoon.com/10-reasons-why-you-should-keep-learning-game-development-hf3l3zmn'
    },
    {
        'id': 1,
        'image': 'https://blogs.unity3d.com/wp-content/uploads/2019/04/Unity-Learn-blog-header_1280x720.jpg',
        'intro': 'Unity Learn provides award-winning free tutorials, sample projects, and full courses for mastering real-time 3D development skills with Unity Learn',
        'type':'websites','name': 'Unity learn',
        'url':  'https://learn.unity.com/'
    },
    {
        'id':2,
        'image': 'https://cdn2.unrealengine.com/Unreal+Engine%2Fonlinelearning-courses%2FNews_UOLDec_fb_image-1200x630-520419d3e9c82ff29459b6844fb50ed0262e715c.jpg',
        'intro': 'Unreal Online Learning is a free learning platform that offers hands-on video courses and guided learning paths.',
        'type':'websites','name': 'unreal engine',
        'url':  'https://www.unrealengine.com/en-US/onlinelearning-courses'
    },
]
Ui_Ux_courses =[
    
    {
        'id': 0,
        'image': 'https://learnux.io/uploads/logo.png',
        'intro': 'User Experience & UI tools are one of the best skills you can get nowadays. UX experts are among most wanted people in the industry with salaries skyrocketing to beat front-end professionals.',
        'name': 'learnux.io',
        'url': 'https://learnux.io/',
        'extra': 'ios design pattrens',
        'price': 'free',
        'type': "UI Design Tools Video Courses",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5bf6e3d14ae3421f52814444_download.jpg',
        'intro': 'Mobbin is a hand-picked collection of the latest mobile design patterns from apps that reflect the best in design. Get inspiration from over 150 iOS apps and 8,000 patterns (screenshots from iPhone X) available on the platform. Sign up to save your favorite patterns.',
        'name': 'mobbin',
        'url': 'https://mobbin.design/',
        'extra': 'ios design pattrens',
        'price': 'free',
        'type': "ios + inspiration",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9c90cc3e5160001ed80f0_fb.png',
        'intro': 'The best design inspiration - expertly curated for you. Muzli is a new-tab Chrome extension that instantly delivers relevant design stories and inspiration. Learn more',
        'name': 'Muzil',
        'url': 'https://muz.li/',
        'extra': 'inspiration',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9c297e87a4d000109e13d_1-t2L7WZC7hpZFexm47qzQSA-p-1600.jpeg',
        'intro': 'Collection of articles, videos, and resources made by designers at Facebook.',
        'name': 'facebook design',
        'url': 'http://facebook.design/',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "inspiration",
    },
    {
        'id': 0,
        'image': 'https://s3.amazonaws.com/www-inside-design/uploads/2015/06/Dribbble-InVision-feature.jpg',
        'intro': 'Dribbble is where designers gain inspiration, feedback, community, and jobs and is your best resource to discover and connect with designers worldwide.',
        'name': 'Dribble',
        'url': 'https://dribbble.com/',
        'extra': 'Ui/Ux',
        'price': 'free',
        'type': "inspiration",
    },
    {
        'id': 0,
        'image': 'https://i.pinimg.com/280x280_RS/e9/f7/e1/e9f7e101e3b7484d53b2b4d5a6004740.jpg',
        'intro': 'Behance is a social media platform owned by Adobe which claims "to showcase and discover creative work"',
        'name': 'Behance',
        'url': 'https://www.behance.net/',
        'extra': 'Ui / ux / animation / design 2d / 3d',
        'price': 'free',
        'type': "inspiration",
    },
    {
        'id': 0,
        'image': 'https://cdn-images-1.medium.com/max/1200/1*A0FnBy5FBoVQC02SZXLXPg.png',
        'intro': 'One-stop resource for everything related to user experience"',
        'name': 'uxplanet',
        'url': 'https://uxplanet.org/',
        'extra': 'ux / animation / design 2d / 3d',
        'price': 'free',
        'type': "inspiration",
    },
    {
        'id': 0,
        'image': 'https://learnux.io/uploads/vectors/figma-course-0.jpg',
        'intro': 'Figma is a revolutionary application, because it maintains its full functionality in both desktop, and browser versions. You can use either of them, and the web version will still surprise you with how efficient it is! Moreover, designing interfaces is but one of its many features. Thanks to its intuitive and user – friendly interface and tool set, everybody is going to be able to edit graphic assets using this app. Figma differs from other, similar applications such as Photoshop and Sketch, mainly because of its amazing collaboration capabilities, where a project may be worked on by more than one person, in real time',
        'name': 'learnux.io',
        'url': 'https://learnux.io/course/figma',
        'extra': 'ios design pattrens',
        'price': 'free',
        'type': "UI Design Tools Video Courses on figma",
    },
]
Machine_learning_courses = [
    {
                'id':0,
                'image': 'https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/18-06s10.jpg',
                'intro': "This is a basic subject on matrix theory and linear algebra. Emphasis is given to topics that will be useful in other disciplines, including systems of equations, vector spaces, determinants, eigenvalues, similarity, and positive definite matrices.",
                'name': "Introduction to Linear Algebra.",
                'Return': 'Base knowledge',
                'type': 'video + youtube',
                'url':  'https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/'
            },
            {
                'id':0,
                'image': 'https://i.ytimg.com/vi/WUvTyaaNkzM/maxresdefault.jpg',
                'intro': "The goal here is to make calculus feel like something that you yourself could have discovered.",
                'name': "Essence of linear calculus",
                'Return': 'Base knowledge',
                'type': 'video + youtube',
                'url':  'https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr'
            },
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/84251067-b212-4355-a9d3-246d91896b90-41bac59be40f.small.jpg',
                'intro': "Build foundational knowledge of data science with this introduction to probabilistic models, including random processes and the basic elements of statistical inference -- Part of the MITx MicroMasters program in Statistics and Data Science",
                'name': "Probability - The Science of Uncertainty and Datassence of linear algebra",
                'Return': 'knowledge',
                'type': 'video + assigments',
                'url':  'https://www.edx.org/course/introduction-probability-science-mitx-6-041x-2'
            },
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/8e285de1-0242-4e94-8041-84231363caf4-e1a05f019d47.small.jpg',
                'intro': "Learn about the core principles of computer science: algorithmic thinking and computational problem solving.",
                'name': "Algorithm Design and Analysis",
                'Return': 'Base knowledge',
                'type': 'video + assigment',
                'url':  'https://www.edx.org/course/algorithm-design-analysis-pennx-sd3x'
            },
             {
                'id':0,
                'image': 'https://i.ytimg.com/vi/kjBOesZCoqc/maxresdefault.jpg',
                'intro': "A geometric understanding of matrices, determinants, eigen-stuffs and more.",
                'name': "Essence of linear algebra",
                'Return': 'Base knowledge',
                'type': 'video + youtube',
                'url':  'https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab'
            },
             {
                'id':0,
                'image': 'https://blog.udacity.com/wp-content/uploads/2015/11/MLND-blog-post-1024x536.png',
                'intro': "This class will teach you the end-to-end process of investigating data through a machine learning lens. Learn online, with Udacity.",
                'name': "Introduction to Machine Learning Course",
                'Return': 'intermidiate knowledge',
                'type': 'video + assigments',
                'url':  'https://www.udacity.com/course/intro-to-machine-learning--ud120'
            },
            {
                'id':0,
                'image': 'https://blog.udacity.com/wp-content/uploads/2015/11/MLND-blog-post-1024x536.png',
                'intro': "A curated list of practical deep learning and machine learning project ideas",
                'name': "Awesome Deep Learning Project Ideas",
                'Return': 'intermidiate knowledge',
                'type': 'practice',
                'url':  'https://github.com/NirantK/awesome-project-ideas'
            },
            {
                'id':0,
                'image': 'https://i.ytimg.com/vi/kjBOesZCoqc/maxresdefault.jpg',
                'intro': "A geometric understanding of matrices, determinants, eigen-stuffs and more.",
                'name': "Essence of linear algebra",
                'Return': 'Base knowledge',
                'type': 'video + youtube',
                'url':  'https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab'
            },
]





@app.route('/programming/courses')
def api_programming_courses():
    return jsonify(Must_programmer_courses)
@app.route('/Ui_Ux/courses')
def api_Ui_Ux_courses():
    return jsonify(Ui_Ux_courses)
@app.route('/gameDevelopment/courses')
def api_gameDevelopment_courses():
    return jsonify(gameDevelopment_courses)
# @courses.route('/Graphic_deginer/courses')
# def api_programming_courses():
#     return jsonify(Graphic_deginer)
@app.route('/webDevelopment/courses')
def api_webDevelopment_courses():
    return jsonify(webDevelopment_courses)
@app.route('/android/courses')
def api_android_courses():
    return jsonify(android_courses)
@app.route('/machine_learning/courses')
def api_Machine_learning_courses():
    return jsonify(Machine_learning_courses)





if __name__ == '__main__':
    app.run()
