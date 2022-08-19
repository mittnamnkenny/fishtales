# FishTales - Fly Fishing Blog

This is my fourth milestone project with Code Institute. FishTales is an Django blog application built for people who enjoy fly fishing. It is targeted towards people fishing in Småland, Sweden. 
The purpose of this site is to allow users to share their fishing stories, upload photos of possible catches as well as comment and like on other posts.

[View the live project here.](https://fishtales-mittnamnkenny.herokuapp.com/)

![Mockup](documentation/amiresponsive.jpg)

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

### Project Goals:
The primary goal for this project is to create a fly fishing blog, that enables full CRUD functionality to register users so that they can Create, Read, Update and Delete both blog posts and comments directly on the site without any delays or intermediaries. The user should have full control over their own posts and that any changes made on the site are directly reflected to the user.

### Strategy:
An Agile methodology was used to plan this project. This was implemented using a Kanban board in GitHub Project with linked Issues. To cover the goals of this project, a total of 5 Epics where created, which were then further developed into 32 User Stories, each with their own acceptance criterias and tasks to complete. Labels where then used to prioritize the importance of each User Story. 28 User Stories were completed working on this project.

The following labels were used in this project and the distribution of user stories by label are:

  - Must-Have: 16/32
  - Should-Have: 7/32
  - Could-Have: 8/32
  - Probably-Won’t-Have: 1/32

For more information: [View the Kanban Board here.](https://github.com/mittnamnkenny/fishtales/projects/1)

### User stories:

  - #### EPIC Admin/Account
    - US1. Account registration and login:
      - As a **Site User** I can **register an account** so that **I can share my fishing stories, comment and like**
    - US2. Manage posts:
      - As a **Site Admin** I can **create, read, update and delete posts and comments** so that **I can manage my blog content**
    - US3. Create drafts:
      - As a **Site Admin** I can **create draft posts** so that **I can finish writing the content later**

  - #### EPIC Post
    - US4. View post list:
      - As a **Site User** I can **view a list of posts** so that **I can easily select one fishing story to read**
    - US5. Open a post:
      - As a **Site User** I can **click on a post** so that **I can read the content**
    - US6. Create post:
      - As a **Site User** I can **create my own posts** and **share my fishing stories**
    - US7. Edit post:
      - As a **Site User** I can **edit my own post** so that **I can update the content**
    - US8. Delete post:
      - As a **Site User** I can **delete my own post** so that **I can interact with the content**
    - US9. View own posts:
      - As a **Site User** I can **view my own posts** so that **I can get a better overview of my fishing stories**
    - US10. Multiple images:
      - As a **Site User** I can **add multiple images to my posts** so that **I can better share my fishing stories and possible catches**
    - US11. Placeholder photos:
      - As a **Site User** the **placeholder photo when creating a post will be based on my fishing location if no photo is uploaded** so the **blog will have more variation in photos**
    - US12. Fish caught:
      - As a **site user** I can **see the number of fish caught without entering the detail page for each post** so that **I can better select interesting posts**
    - US13. Weather info:
      - As a **site user** I can **see the weather conditions without entering the detail page for each post** so that **I can better select interesting posts**
    - US14. Number of comments:
      - As a **site user** I can **see the number of comments without entering the detail page for each post** so that **I can better select interesting posts**
    - US15. Number of likes:
      - As a **site user** I can **see the number of likes without entering the detail page for each post** so that **I can better select interesting posts**
    - US16. Restrict delete post:
      - As a **site user** I will **be prevented from deleting my own post if any comments have been made** so that **comments are protected and people are encouraged to comment more**
    - US17. Restrict blog view:
      - As a **site user** I will **not be able to view the blog content without signing in** so that **more users will register to the site**

  - #### EPIC Like
    - US18. View likes:
      - As a **Site User** I can **view the number of likes on each post** so that **I can see which is the most popular or viral**
    - US19. Like:
      - As a **Site User** I can **like a post** so that **I can interact with the content**
    - US20. Downvote:
      - As a **Site User** I can **downvote a post** so that **I can interact with the content**

  - #### EPIC Comment
    - US21. View comments:
      - As a **Site User** I can **view comments on an individual post** so that **I can read the conversation**
    - US22. Comment on a post:
      - As a **Site User** I can **leave comments on a post** so that **I can be involved in the conversation**
    - US23. Delete Comment:
      - As a **Site User** I can **delete my own comment** so that **I can interact with the content**
    - US24. Edit comment:
      - As a **Site User** I can **edit my own comment** so that **I can update the content**

  - #### EPIC UX/UI/ETC
    - US25. Responsive:
      - As a **Site User** I can **use the site on the following platforms: desktop, laptop, tablet and smartphone** so that **I can access all functionality**
    - US26. Design:
      - As a **Site User** I can **get an overall positive impression based on the principles of user experience design, accessibility and responsivity** so that **I can quickly determine the purpose of the site and enjoy using it**
    - US27. System messages:
      - As a **Site User** I will **get system messages when I interact with the site** so that **I get feedback when actions are completed**
    - US28. Hero image:
      - As a **Site User** I am **presented with a hero image** so that **I can clearly see the purpose of the site**
    - US29. Featurette:
      - As a **Site User** I am **presented with a featurette** so that **I can better understand the site’s purpose**
    - US30. Favicon:
      - As a **Site User** I am **presented with a favicon** so that **I can get a better experience when browsing with multiple tabs**
    - US31. Carousel:
      - As a **Site User** I can **view a carousel with new posts** so that **I can easily see any post updates to the blog**
    - US32. GitHub:
      - As a **Site User** I am **presented with a link to mittnamnkenny’s GitHub** so that **I can view more repositories**

  - #### User Stories not implemented
    - US9. View own posts:
      - This user story was prioritized as a could-have feature and will not be implemented at this stage due to low priority.
    - US16. Restrict delete post:
      - This user story was prioritized as a could-have feature and will not be implemented. I want the post author to have full control over their own posts.
    - US17. Restrict blog view:
      - This user story was prioritized as a Probably-Won’t-Have feature and will not be implemented. I want unregistered users to be able to view the blog content before choosing to register.
    - US20. Downvote:
      - This user story was prioritized as a could-have feature and will not be implemented. I do not think this contributes to an overall positive experience; the upvote functionality is enough for this purpose.

## Features



## Design



## Technologies Used



## Testing



## Deployment



## Credits 