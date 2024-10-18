**AdaptiveReview** is a hybrid spaced repetition system designed for effective single-session review. It combines principles of adaptive learning and interval-based repetition to enhance retention by dynamically adjusting review priorities based on performance. 

### How It Works:
1. **Box 0 (Missed Questions):** 
   - If a question is answered incorrectly, it moves to Box 0. 
   - These questions are prioritized for immediate review, especially if more than **60 seconds** have passed since they were last seen, ensuring quick reinforcement of challenging content.
   
2. **Box 1 (Unasked Questions):** 
   - This box holds all questions that have not yet been presented. 
   - When there are no immediate review needs in Box 0, new questions are drawn from Box 1. Correct answers move these questions to Box 2, while incorrect answers redirect them to Box 0.

3. **Box 2 (Correctly Answered Once):** 
   - Questions that have been answered correctly once are placed here. 
   - They are scheduled for review if **360 seconds** have elapsed since they were last asked, reinforcing learning at slightly longer intervals. Correct responses move them to Box 3, while errors send them back to Box 0.

4. **Box 3 (Known Questions):** 
   - Questions that have been answered correctly twice are placed in this box. 
   - These are considered "mastered" and are only reviewed if all other boxes are empty, preventing unnecessary repetition.

### Benefits:
AdaptiveReview incorporates a **temporal element** by managing when to review questions based on time elapsed and user performance, enhancing retention within a single session. It ensures that difficult questions receive focused, immediate attention while progressively spacing out reviews for content that has been successfully learned. 

By combining the adaptive approach of real-time feedback with the structured intervals of spaced repetition, AdaptiveReview provides an efficient and effective method for reinforcing knowledge in a single study session.