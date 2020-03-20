# Data Analysis for Marketing

## Instructor Prep

### Lesson Overview

Today's lecture focuses on using Data Analysis and Visualization tools to drive forward business solutions, with a focus on marketing. This class focuses on translating some of the skills that students have covered in the course into real world interview success.

### Class Objectives

By the end of this class, students will be able to:

* Demonstrate ability to apply technical skills to analyze data in a manner that adds business value.
* Explore applications of data analysis for marketing teams.

- - -

## Lecture Content

Follow along with the [Data Analysis for Marketing slide deck](https://docs.google.com/presentation/d/1ssuYbYefIcWHKs5XLQj5EXjzneW1OX5ip-VSvgrAvNQ/edit#slide=id.gc6f919934_0_0). Each slide is represented by a drop down menu.

### 1. Welcome & Overview (10 mins)

<details>
   <summary><strong>Slide 1: Welcome/Title</strong></summary>

* Welcome students to todays webinar. Feel free to open up with an icebreaker, such as "Popcorn".

  * To play Popcorn, Introduce yourself to the class, then choose a student to introduce themselves. Have them call on another, and so on until all students have introduced themselves or more than 5 minutes has gone by.

  * One way to encourage engagement is to ask students to name a fun fact along with their introduction, maybe even specify their favorite animal/song/vacation spot? Feel free to add a personal touch.

</details>

<details>
   <summary><strong>Slide 2: Prerequisite Knowledge</strong></summary>

* Before diving into content, let's take this opportunity to see how the class is feeling about each one of the following topics.

* Using fist-to-five, with fist meaning <code>"I'm completely lost - I have no understanding of what's going on or where I am"</code> and five meaning <code>"I AM THE CODE!!"</code> tell me how you feel about:

  * Python
  * Linear Regression
  * Data Cleaning
  * Exploratory Data Analysis (EDA)

* Encourage students who are less confident about their skill levels to participate in office hours. Use this opportunity to remind them that tutoring is also included with the Boot Camp.

</details>

<details>
   <summary><strong>Slide 3: Overview</strong></summary>
  
* Today we will be learning how to apply some of our newfound Data Analysis and Visualization skills to drive forward business solutions.

* This lecture will primarily focus on how we can use Data to support a Marketing team.

* It is highly likely that when you interview for real world Data jobs, that you will be asked to develop on-the-fly solutions to practical business problems.

* The ability to demonstrate the application of technical skills to answer business and marketing questions could be the key to a successful interview and a new career.

</details>

<details>
   <summary><strong>Slide 4: Marketing Analytics</strong></summary>

* Encourage students that enjoy the content of this lecture to look into Marketing Analytics as a potential future career move.

* Many of the skills learned in this course translate directly to the role of a Marketing Analyst. Applicable skills include:

  * Data Visualization
  * Data Queries
  * Creating Stories from Data
  * Deriving Data-Driven Insights
  * Coding
  * Analytics Tools

</details>

### 2. Understanding Marketing (10 mins)

<details>
   <summary><strong>Slide 5: Marketing Vocabulary</strong></summary>

* In order for students to fully grasp the concepts covered in today's lecture and to prepare them to speak the lingo if they find themselves preparing data for a marketing department, it is important to cover a few key vocabulary terms.

* Share [marketing_vocab.pdf](./marketing_vocab.pdf) with class as reference material. Open link on screen and choose and few important keywords to highlight.

</details>

<details>
   <summary><strong>Slide 6: Why is Marketing Important?</strong></summary>

* It can be argued that Marketing is the single most important factor in determining whether or not a business will succeed.

* Marketing departments buy ads, write copy, bid on keywords, organize events, and identify target demographics to market to.

* In other words, they are responsible for engagement strategies and maintainining relationships with their audience.

</details>

<details>
   <summary><strong>Slide 7: What is Data Driven Marketing?</strong></summary>

* Data Driven Marketing is the process of using available data to gain industry and performance insights, in turn allowing the business to make more informed marketing decisions.

* Run class through the four part process listed in the chart and ask students if they can relate this process to the processes that they've covered in class

* Use the following as some potential examples of marketing problems that require Data Driven solutions:

  * "Some of our KPIs seems to be decreasing, could you help us determine what may be leading to this sudden decline in performance?"
  * "Could you gather data to help us determine which marketing efforts are driving the highest amount of conversions?"

* Make sure to highlight this potential issue, as it will be followed up in the next section:

  * “Our CPA is pretty high and we want to invest in clients with the highest Lifetime value. Can you help us?”

</details>

<details>
   <summary><strong>Slide 8: Data Driven Marketing Gets Results</strong></summary>

* Data Driven Marketing has completely reshaped the way that companies engage with customers, design marketing campaigns, and determine which assets are critical and worth continuing to expense.

  * Explain that DDM has been shown to improve Efficiency, Engagement, and Performance when applied to marketing strategy.

* There are many inspiring statistics to vouch for the relevance and importance of DDM. Let's take some time to highlight a few of the best:

  * Companies that utilize DDM are 6 times more likely to be profitable.
  * Businesses with data-driven strategies have five to eight times as much ROI.
  * 40% of brands plan to expand their DDM budgets.
  * Marketers that exceeded revenue goals used Data Driven Personalization 83% of the time.
  * 64% of marketing executives "strongly agree" that DDM is crucial to business.

</details>

### 3. Applying Data Analytics (10 mins)

<details>
   <summary><strong>Slide 9: Begin to Apply Data Analytics</strong></summary>

* The first step in solving any problem is to rephrase it in terminology that works for you. Let's use this question from earlier for example:

  * “Our CPA is pretty high and we want to only invest in clients with the highest LTV. Can you help us?”

* Let's remove all irrelevant content so that we can focus on what data we actually need to be gathering.

* How could we re-phrase this question in Data terms?

  * “What traits do customers with high LTV share?”

</details>

<details>
   <summary><strong>Slide 10: Redefine the Issue in Data Terms</strong></summary>

* The first step in solving any problem is to rephrase it in terminology that works for you. Let's use this question from earlier for example:

  * “Our CPA is pretty high and we want to only invest in clients with the highest LTV. Can you help us?”

* Let's remove all irrelevant content so that we can focus on what data we actually need to be gathering.

* How could we re-phrase this question in Data terms?

  * “What traits do customers with high LTV share?”

</details>

<details>
   <summary><strong>Slide 11: Acquire the Data</strong></summary>

* The best place to start in this case is probably to ask marketing where they store data.

  * Let's imagine for this example that they use SalesForce and for some reason you can’t access it.

  * No problem! Have them
run a fresh report and send over a <code>.csv</code> file.

</details>

<details>
   <summary><strong>Slide 12: Pull Data into Jupyter Notebook</strong></summary>

* Let's use Python code to import our CSV file into a Jupyter Notebook:

</details>

### 4. Clean and Present your Data (10 mins)

<details>
   <summary><strong>Slide 13: Clean the Data</strong></summary>

* **Ask the Class:** What should we do if 5 of 1,000,000 records are missing age, but we suspect that Age is relevant to CLTV?
  * **Answer:** A quantity this small shouldn't matter enough to throw off such a large sample size. If age is relevant, it is probably best to just throw away these five outliders.
  * We definitely don't want to remove columns that have relevant data.
  * If 50% of data was missing age, we would keep all of those clients' data without the age column, to prevent from losing such a huge amount of Data.

</details>

<details>
   <summary><strong>Slide 14: Exploratory Data Analysis (EDA)</strong></summary>

* Let's use some more Python code to plot our data and analyze CLTV against each other factor listed in the CSV.

* Our goal is to use regression analysis to look for the strongest correlations between our various criteria and CLTV.

</details>

<details>
   <summary><strong>Slide 15: Present Findings to Stakeholders</strong></summary>

* Consider employer needs when assembling a presentation from your findings.

  * What are the real problems facing marketing teams?

  * Are they worried about lifetime value, or value in the next year?

* Make it your goal to always exceed employer expectations and go the extra step.

  * Perhaps, in your Analysis, you stumble upon information that you know could be highly valuable to your company. Don't hesitate to include it just because it isn't specifically what you are solving for!

</details>

<details>
   <summary><strong>Slide 16: Student Questions and End Lecture</strong></summary>

* Take one more "Fist-to-Five" of the class to see how they feel about the material that you just went over.

* If time permits, allow them time to ask any lingering questions that they may have. If you know that it will take a lengthy response or a group search to find an answer for a student, refer the student to office hours and move along.

* Thank the class for their time and participation, and ask them to fill out the feedback form that you will be Slacking out if they get a chance.

</details>
