# PawPal+ Project Reflection

## 1. System Design

- User must be able to create tasks and edit them at will 
- User needs a daily plan based on the provided constraints such as time 
- User's daily plan must include tasks that were mentioned once but have to be repeated, this could be an option when creating a task 

- Pet Class 
- User/Owner Class
- Tasks Class 
- Schedule Class 

Attributes 
Pet Class: Name, type of animal, age, dietary restrictions, breed, vet, tasks list, medications, tasks, id
Schedule: Days of Week, Time blocked, Time Free, tasks to schedule
Tasks: Pet, task description, repeat task (boolean), task completed, priority, location of task, task duration, task scheduled time, task id 
Owner: Number of pets, Schedule, Number of tasks, preferences, pet list, tasks list  

Methods
Pet Class: Get pet information (include medication), get task list, add task, remove task
Schedule: add free time, block time for task, block time for repeated task, add busy time, reschedule tasks, get upcoming tasks for day, get upcoming tasks for week, get upcoming tasks for month, change time for a repeated task once, change time for a task, 
Tasks: Add/remove tasks, mark task completed, change priority of tasks,
Owner: add/remove pet, get schedule, generate schedule for all pets, add time constraints, generate schedule for one pet, add/remove preferences 

Relation ship between classes 
Tasks -> Pet -> Owner 
Schedule -> Owner 


**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
