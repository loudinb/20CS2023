# Revised Comprehensive Requirements Document for Instagram-like App

## 1. Introduction

This document outlines the comprehensive requirements for an Instagram-like application developed using Python. The application aims to provide core functionalities similar to Instagram, focusing on user management, post creation and management, social interactions, and direct messaging.

## 2. User Management

### 2.1 User Registration
- Users must be able to create an account with a unique username and email.
- Usernames must meet the following criteria:
  - Length: 3-30 characters
  - Allowed characters: letters, numbers, periods, and underscores
- Emails must be valid and unique within the system.

### 2.2 User Profiles
- Users must be able to set and update a bio (maximum 150 characters).
- Users must be able to view their own posts, follower count, and following count.
- The system must track and display the number of posts a user has made.

## 3. Post Management

### 3.1 Post Creation
- Users must be able to create posts with text content (maximum 2,200 characters).
- Posts must be associated with the user who created them.
- Posts must have a timestamp indicating when they were created.
- Users must be able to add tags to their posts (maximum 30 characters per tag, alphanumeric only).

### 3.2 Post Editing
- Users must be able to edit the content of their own posts after creation.
- Users must be able to add or remove tags from their own posts after creation.

### 3.3 Post Deletion
- Users must be able to delete their own posts.
- When a post is deleted, all associated comments and likes must also be removed.

### 3.4 Post Viewing
- Users must be able to view their own posts.
- Users must be able to view posts from users they follow in a chronological feed.

## 4. Social Interactions

### 4.1 Following
- Users must be able to follow other users.
- Users must be able to unfollow users they are currently following.
- The system must maintain an accurate count of followers and following for each user.

### 4.2 Likes
- Users must be able to like posts.
- Users must be able to unlike posts they have previously liked.
- The system must maintain an accurate count of likes for each post.

### 4.3 Comments
- Users must be able to comment on posts (maximum 2,200 characters per comment).
- Comments must be associated with both the post and the user who made the comment.
- Comments must have a timestamp indicating when they were created.
- Users must be able to delete their own comments on any post.
- Users must be able to delete any comments on their own posts.

### 4.4 User Feed
- Users must be able to view a feed of posts from users they follow.
- The feed should be in reverse chronological order (newest posts first).

## 5. Content Discovery

### 5.1 Tagging
- Users must be able to add multiple tags to a post when creating or editing it.
- Tags must be alphanumeric and no longer than 30 characters.

### 5.2 Searching
- Users must be able to search for posts by tags.
- The system must return all posts associated with a searched tag.

## 6. Direct Messaging

### 6.1 Sending Messages
- Users must be able to send private messages to other users.
- Messages must have a maximum length of 2,000 characters.

### 6.2 Viewing Messages
- Users must be able to view messages sent to and from them.
- Messages must be displayed in chronological order.

## 7. Data Management

### 7.1 User Data
- The system must keep track of each user's posts, followers, and following list.
- The system must maintain an accurate count of posts, followers, and following for each user.

### 7.2 Post Data
- The system must store each post's content, author, timestamp, tags, likes, and comments.

### 7.3 Message Data
- The system must store each message's sender, recipient, content, and timestamp.

## 8. Performance and Scalability

- The application should be able to handle multiple users simultaneously (exact number not specified in this version).
- The application should respond to user actions in a timely manner (specific response times not defined in this version).

## 9. Security

- Users should only be able to modify their own data (posts, profile information).
- The system must ensure that private messages are only viewable by the sender and recipient.

## 10. Error Handling

- The system must provide appropriate error messages for invalid actions (e.g., trying to follow a user that doesn't exist).
- The system must handle and recover from unexpected errors without crashing.
