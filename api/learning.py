from flask import Blueprint
from flask import Flask, request, jsonify
learning = Blueprint("learning", __name__)
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
gameDevelopment= [
        {
        'id': 0,
        'image': 'https://hackernoon.com/drafts/1k3j3zqp.png',
        'intro': '10 Reasons Why You Should Learn How To Develop Video Games',
        'url': 'https://hackernoon.com/10-reasons-why-you-should-keep-learning-game-development-hf3l3zmn'
    },
    {
        'id': 1,
        'image': 'https://blogs.unity3d.com/wp-content/uploads/2019/04/Unity-Learn-blog-header_1280x720.jpg',
        'intro': 'Unity Learn provides award-winning free tutorials, sample projects, and full courses for mastering real-time 3D development skills with Unity Learn',
        'name': 'Unity learn',
        'url':  'https://learn.unity.com/'
    },
    {
        'id':2,
        'image': 'https://cdn2.unrealengine.com/Unreal+Engine%2Fonlinelearning-courses%2FNews_UOLDec_fb_image-1200x630-520419d3e9c82ff29459b6844fb50ed0262e715c.jpg',
        'intro': 'Unreal Online Learning is a free learning platform that offers hands-on video courses and guided learning paths.',
        'name': 'unreal engine',
        'url':  'https://www.unrealengine.com/en-US/onlinelearning-courses'
    },
]
webDevelopment = [
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
                'image': 'https://images.ctfassets.net/aq13lwl6616q/4tUaHeYUpOP2f5Tv5dTX0F/2ecfc593dae0f7f439501c01e321285b/image.png?w=800&h=669&q=50&fm=webp',
                'intro': "Broswer game to practice identifying HTML selectors for use in CSS stylesheets.",
                'name': "CSS Diner",
                'type': 'css Games',
                'url':  'https://css-diner.netlify.app/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/72nixprDE0M0fwwMkQZbYN/7ce860cb66c6f22eedd8913108d70d2a/image.png?w=636&h=300&q=50&fm=webp',
                'intro': "A browser game where you write CSS code to help you learn CSS grid layout.",
                'name': "Grid Garden",
                'type': 'css Games',
                'url':  'https://cssgridgarden.com/'
            },
            {
                'id':0,
                'image': 'https://images.ctfassets.net/aq13lwl6616q/58rc7QCmF0ifFvXxUhsi0l/35dcdd264a17a62f830b9584b8d866e1/image.png?w=636&h=300&q=50&fm=webp',
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
Ui_Ux = [
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
        'into': 'Collection of articles, videos, and resources made by designers at Facebook.',
        'name': 'facebook design',
        'url': 'http://facebook.design/',
        'extra': 'Human illustrations',
        'price': 'free',
        'type': "learning",
    },
    
]
programming =[
    {
        'id': 0,
        'image': 'https://miro.medium.com/max/1909/1*ywYwvB-aydv0Ovx7K-5P3g.jpeg',
        'intro': "A new take on the age-old question: Should you rewrite your application from scratch, or is that “the single worst strategic mistake that any software company can make”? ",
        'name': 'Lessons from 6 software rewrite stories',
        'url': 'https://medium.com/@herbcaudill/lessons-from-6-software-rewrite-stories-635e4c8f7c22',
        },
    {
        'id': 0,
        'image': 'https://cdn-media-1.freecodecamp.org/images/1*3pyJUEclXtPt8TNONerTUg.jpeg',
        'intro': "How to escape tutorial purgatory as a new developer — or at any time in your career.",
        'name': 'For a long time I held off from starting my own side projects because of how much I didn’t know how to do.',
        'url': 'https://www.freecodecamp.org/news/how-to-escape-tutorial-purgatory-as-a-new-developer-or-at-any-time-in-your-career-e3a4b2384a40/',
    },
    {
        'id': 0,
        'image': 'https://cdn-media-1.freecodecamp.org/images/1*3pyJUEclXtPt8TNONerTUg.jpeg',
        'intro': "How to escape tutorial purgatory as a new developer — or at any time in your career.",
        'name': 'For a long time I held off from starting my own side projects because of how much I didn’t know how to do.',
        'url': 'https://www.freecodecamp.org/news/how-to-escape-tutorial-purgatory-as-a-new-developer-or-at-any-time-in-your-career-e3a4b2384a40/',
    },
    {
        'id': 0,
        'image': 'https://cdn-media-1.freecodecamp.org/images/1*3pyJUEclXtPt8TNONerTUg.jpeg',
        'intro': "How to escape tutorial purgatory as a new developer — or at any time in your career.",
        'name': 'For a long time I held off from starting my own side projects because of how much I didn’t know how to do.',
        'url': 'https://www.freecodecamp.org/news/how-to-escape-tutorial-purgatory-as-a-new-developer-or-at-any-time-in-your-career-e3a4b2384a40/',
    },
]
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
@learning.route('/programming/learning')
def api_programming_learning():
    return jsonify(programming)
@learning.route('/Ui_Ux/learning')
def api_Ui_Ux_learning():
    return jsonify(Ui_Ux)
@learning.route('/gameDevelopment/learning')
def api_gameDevelopment_learning():
    return jsonify(gameDevelopment)
# @learning.route('/Graphic_deginer/learning')
# def api_programming_learning():
#     return jsonify(Graphic_deginer)
@learning.route('/webDevelopment/learning')
def api_webDevelopment_learning():
    return jsonify(webDevelopment)
@learning.route('/android/learning')
def api_android_learning():
    return jsonify(android)
@learning.route('/machine_learning/learning')
def api_machine_learning_learning():
    return jsonify(Machine_learning)