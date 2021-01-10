from api.api import Machine_courses, Must_programmer
from flask import Blueprint
from flask import Flask, request, jsonify
courses = Blueprint("courses", __name__)
android = [
            {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/8f8e5124-1dab-47e6-8fa6-3fbdc0738f0a-762af069070e.small.jpg',
                'intro': "This course picks up where CS50 leaves off, diving more deeply into the design and implementation of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap.",
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
webDevelopment = [
    {
                'id':0,
                'image': 'https://prod-discovery.edx-cdn.org/media/course/image/8f8e5124-1dab-47e6-8fa6-3fbdc0738f0a-762af069070e.small.jpg',
                'intro': "This course picks up where CS50 leaves off, diving more deeply into the design and implementation of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap.",
                'name': "CS50's Web Programming with Python and JavaScript",
                'Return': 'free certificate',
                'type': 'video + assigment',
                'url':  'https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript'
    },
    {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png?w=636&h=300&q=50&fm=webp',
                'intro': "From the basics to advanced topics with simple, but detailed explanations.",
                'name': "The Modern JavaScript Tutorial",
                'type': 'text',
                'url':  'http://javascript.info/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/4RGBWl2tZ0bYIt0GX7XVw1/25f59ffd9052d12bba2a4f562c2ff25f/image.png?w=636&h=300&q=50&fm=webphttps://images.ctfassets.net/aq13lwl6616q/4RGBWl2tZ0bYIt0GX7XVw1/25f59ffd9052d12bba2a4f562c2ff25f/image.png?w=636&h=300&q=50&fm=webp',
                'intro': "Guide for JavaScript & Node.js reliability from A-Z.",
                'name': "Testing JavaScript: Best Practices",
                'type': 'free templates',
                'url':  'https://github.com/goldbergyoni/javascript-testing-best-practices'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png?w=636&h=300&q=50&fm=webp',
                'intro': "From the basics to advanced topics with simple, but detailed explanations.",
                'name': "The Modern JavaScript Tutorial",
                'type': 'free templates',
                'url':  'http://javascript.info/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/3SsqQsiuKq2G0RQwHxCIFS/8b75c7ae088313fe7b7a13760dd24378/image.png?w=636&h=300&q=50&fm=webp',
                'intro': "From the basics to advanced topics with simple, but detailed explanations.",
                'name': "The Modern JavaScript Tutorial",
                'type': 'free templates',
                'url':  'http://javascript.info/'
            },
            

]
Must_programmer = [
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/33tbBpGanLQYMSxpnkL7nC/02bc0ffd5053dd8b0b146faa145f37f2/Git_Branching.PNG?w=800&h=387&q=50&fm=webp',
        'intro':'Coursera Course (Not CS Specific) teach you how the mind grasp thing and how to train it to learn things as convinient and fast as possible',
        'name': 'Learn Git Branching Interactively',
        'url': 'https://www.coursera.org/learn/learning-how-to-learn'
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/33tbBpGanLQYMSxpnkL7nC/02bc0ffd5053dd8b0b146faa145f37f2/Git_Branching.PNG?w=800&h=387&q=50&fm=webp',
        'intro':'The most visual, interactive and fun way to learn Git on the web.',
        'name': 'Learn Git Branching Interactively',
        'url': 'https://learngitbranching.js.org/'
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5qFgoOTACYlbYpc2pPlqjM/a0f2662b4e2a3bfc2fc30c84b7f6e963/1500x500?w=800&h=267&q=50&fm=webp',
        'intro':'Find the right git commands you need without digging through the web.',
        'name': 'Git Command Explorer',
        'url': 'https://gitexplorer.com/'
    },

    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/5qFgoOTACYlbYpc2pPlqjM/a0f2662b4e2a3bfc2fc30c84b7f6e963/1500x500?w=800&h=267&q=50&fm=webp',
        'intro':'Free individual licenses of the award-winning professional developer tools from JetBrains for students and faculty members.',
        'name': 'JetBrains Student License',
        'url': 'https://www.jetbrains.com/student/'
    },
    


    
    {
        'id': 0,
        'image': 'https://github.blog/wp-content/uploads/2014/10/4b0317bc-4599-11e4-8bc3-0ca4dd5223e8.png?resize=2284%2C889',
        'intro':'There’s no substitute for hands-on experience, but for most students, real world tools can be cost prohibitive. That’s why github created the GitHub Student Developer Pack with some of there partners and friends: to give students free access to the best developer tools in one place so they can learn by doing',
        'name': 'GitHub Student Developer Pack',
        'url': 'https://education.github.com/'
    },
    {
        'id': 0,
        'image': 'https://149351115.v2.pressablecdn.com/wp-content/uploads/2017/02/college-degrees-1024x395.jpg',
        'intro':'Do developers need college degrees? Just a generation ago, it was a given that a college degree was the best way to maximize the likelihood of securing a high-paying job in the field of your choice. But the world has changed, and more and more you hear of successful developers who never earned a degree,',
        'name': 'Do Developers Need College Degrees?',
        'url': 'https://stackoverflow.blog/2016/10/07/do-developers-need-college-degrees/?fbclid=IwAR1H9tBaYd1zGUIam6nVQovHcJETHwoo11VHBlV8peR0JO8PJNgAHMsQqvw'
    },
    {
                'id':0,
        'image': 'https://online-learning.harvard.edu/sites/default/files/styles/social_share/public/course/cs50x-original.jpg?itok=kR_JV8DW',
        'intro': 'An entry-level course taught by David J. Malan, CS50x teaches students how to think algorithmically and solve problems efficiently.',
        'name': 'cs50',
        'Return': 'free certificate',
        'url':  'https://www.edx.org/course/cs50s-introduction-to-computer-science'
    },
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/6YUQllDI9KrCgiZy8GsMnZ/c38322baa2bfc2d8af1f6ca19ae6e564/maxresdefault.jpg?w=800&h=450&q=50&fm=webp',
        'intro':'This tutorial will teach you modern git and Github',
        'name': 'In Depth Tutorial on Git & Github (DevOps Tools)',
        'url': 'https://www.youtube.com/watch?v=6bjCvZEX52w'
    },
    {
        'id': 0,
        'image': 'https://pr.azureedge.net/img/picresize_logo_registered.png',
        'intro': "visual representaiton of Diffrent Algorithms",
        'name': 'Visual Algo',
        'url': 'https://visualgo.net/en',
    }
    ,
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/6lslLWTrtJOvT9uKL76BdA/c68fa37469f4052acc66944843ba310a/image.png?w=300&h=168&q=50&fm=webp',
        'intro': "Better understand how far computers have taken us and how far they may carry us.",
        'name': 'Crash Course Computer Science',
        'url': 'https://www.youtube.com/watch?v=tpIctyqH29Q&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo',
    }
    ,
    {
        'id': 0,
        'image': 'https://images.ctfassets.net/aq13lwl6616q/2MdYGTNWLQ4qpBn9lv6Npy/700fed96c05f8149567c70aa871f9bd7/maxresdefault.jpg?w=800&h=450&q=50&fm=webp',
        'intro': "The latest edition of the fantastic, free computer science lectures from Harvard.",
        'name': 'Cs50 2020',
        'url': 'https://youtu.be/Tpl7k8IOT6E',
    }
]
gameDevelopment = [
    {
        'id': 0,
        'image': 'https://www.telcoma.in/en/wp-content/uploads/2019/09/Mastering-Data-Structures-Algorithms-using-C-and-C0-.jpg',
        'intro': "Download Free Your Desired AppIntroduction to Algorithms Introduction to course. Why we write Algorithm? Who writes Algorithm? When Algorithms are written? Differences between Algorithms and Programs",
        'sum+up': "Youtube videos",
        'name': 'Abdul Bari: YouTubeChannel for Algorithms',
        'url': 'https://www.youtube.com/watch?v=0IAPZzGSbME&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=2&t=0s',
    },
    {
        'id': 0,
        'image': 'https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190529171221/Learning-Data-Structures-and-Algorithms-is-Important1-1024x424.png',
        'intro': "Hey guys, we have created this channel to provide quality education to students who want to learn, grow and do something beautiful with their life",
        'sum+up': "Youtube videos",
        'name': 'Data Structures and algorithms',
        'url': 'https://www.youtube.com/watch?v=lxja8wBwN0k&list=PLKKfKV1b9e8ps6dD3QA5KFfHdiWj9cB1s',
    },
    {
        'id': 0,
        'image': 'https://miro.medium.com/max/1024/1*9QRFQdpO2f59GsN2KsE9XA.png',
        'intro': "Data Structure & Algorithms course is the most easiest way, that also at free of cost. This playlist has been created by WsCube Tech to help you learn and understand the concepts of Data Structure Algorithm(DSA). All videos cover a wide range of topics and explain each topic with practical examples. You can easily learn about Data Structure Algorithm(DSA), Subscribe the channel to get the latest videos. ",
        'sum+up': "Youtube videos(Hindi)",
        'name': 'Data Structures and algorithms Course',
        'url': 'https://www.youtube.com/playlist?list=PLmGElG-9wxc9Us6IK6Qy-KHlG_F3IS6Q9',
    },
    {
        'id': 0,
        'image': 'https://miro.medium.com/max/1024/1*9QRFQdpO2f59GsN2KsE9XA.pnghttps://i.ytimg.com/vi/CvSOaYi89B4/maxresdefault.jpg',
        'intro': "What are algorithms and why should you care? We'll start with an overview of algorithms and then discuss two games that you could use an algorithm to solve more efficiently - the number guessing game and a route-finding game.",
        'sum+up': "videos + exersise",
        'name': 'Khan Academy',
        'url': 'https://www.khanacademy.org/computing/computer-science/algorithms',
    },
    {
        'id': 0,
        'image': 'https://miro.medium.com/max/1000/0*ZzOeJHpQQk4RhhWW.png',
        'intro': " Pre-requisite for this lesson is good understanding of pointers in C. In this series of lessons, we will study and implement data structures. We will be implementing these data structures in c or c++.  Pre-requisite for this lesson is good understanding of pointers in C. Watch this series on pointers before starting on this series: ",
        'sum+up': "Youtube videos",
        'name': 'Data structures by mycodeschool',
        'url': 'https://www.youtube.com/playlist?list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P',
    },
]
Ui_Ux =[
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/5bf6e3d14ae3421f52814444_download.jpg',
        'into': 'Mobbin is a hand-picked collection of the latest mobile design patterns from apps that reflect the best in design. Get inspiration from over 150 iOS apps and 8,000 patterns (screenshots from iPhone X) available on the platform. Sign up to save your favorite patterns.',
        'name': 'mobbin',
        'url': 'https://mobbin.design/',
        'extra': 'ios design pattrens',
        'price': 'free',
        'type': "ios + inspiration",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9c90cc3e5160001ed80f0_fb.png',
        'into': 'The best design inspiration - expertly curated for you. Muzli is a new-tab Chrome extension that instantly delivers relevant design stories and inspiration. Learn more',
        'name': 'Muzil',
        'url': 'https://muz.li/',
        'extra': 'inspiration',
        'price': 'free',
        'type': "Resource",
    },
    {
        'id': 0,
        'image': 'https://uploads-ssl.webflow.com/59e09526e2711e000116d446/59e9c297e87a4d000109e13d_1-t2L7WZC7hpZFexm47qzQSA-p-1600.jpeg',
        'into': 'Collection of articles, videos, and resources made by designers at Facebook.',
        'name': 'facebook design',
        'url': 'http://facebook.design/',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "inspiration",
    },
    {
        'id': 0,
        'image': 'https://s3.amazonaws.com/www-inside-design/uploads/2015/06/Dribbble-InVision-feature.jpg',
        'into': 'Dribbble is where designers gain inspiration, feedback, community, and jobs and is your best resource to discover and connect with designers worldwide.',
        'name': 'Dribble',
        'url': 'https://dribbble.com/',
        'extra': 'Ui/Ux',
        'price': 'free',
        'type': "inspiration",
    },
    {
        'id': 0,
        'image': 'https://i.pinimg.com/280x280_RS/e9/f7/e1/e9f7e101e3b7484d53b2b4d5a6004740.jpg',
        'into': 'Behance is a social media platform owned by Adobe which claims "to showcase and discover creative work"',
        'name': 'Behance',
        'url': 'https://www.behance.net/',
        'extra': 'Ui / ux / animation / design 2d / 3d',
        'price': 'free',
        'type': "inspiration",
    },
    {
        'id': 0,
        'image': 'https://cdn-images-1.medium.com/max/1200/1*A0FnBy5FBoVQC02SZXLXPg.png',
        'into': 'One-stop resource for everything related to user experience"',
        'name': 'uxplanet',
        'url': 'https://uxplanet.org/',
        'extra': 'ux / animation / design 2d / 3d',
        'price': 'free',
        'type': "inspiration",
    }
]
Machine_learning = [
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
@courses.route('/programming/courses')
def api_programming_courses():
    return jsonify(Must_programmer)
@courses.route('/Ui_Ux/courses')
def api_Ui_Ux_courses():
    return jsonify(Ui_Ux)
@courses.route('/gameDevelopment/courses')
def api_gameDevelopment_courses():
    return jsonify(gameDevelopment)
# @courses.route('/Graphic_deginer/courses')
# def api_programming_courses():
#     return jsonify(Graphic_deginer)
@courses.route('/webDevelopment/courses')
def api_webDevelopment_courses():
    return jsonify(webDevelopment)
@courses.route('/android/courses')
def api_android_courses():
    return jsonify(android)
@courses.route('/Machine_learning/courses')
def api_Machine_learning_courses():
    return jsonify(Machine_learning)