--------------------------------------------------
File-Based To-Do List Manager
--------------------------------------------------
Approach:
- Extended the Week 1 To-Do List program.
- Added functionality to save tasks into a JSON/text file.
- On program start, it automatically loads tasks from the saved file.
- User can add, update, mark complete, or delete tasks.

How to Run:
1. Run the Python file in terminal/IDE.
2. On startup, existing tasks will be loaded.
3. Perform operations (add/view/complete/delete).

Example Input/Output:
Input: Add Task → "Complete Assignment"
Output: Task added successfully!

Input: View Tasks
Output: [1] Complete Assignment (Pending)

Challenges Faced:
- Handling file reading/writing correctly.
- Ensuring tasks don’t get lost when the program restarts.
- Managing JSON formatting errors.
--------------------------------------------------


--------------------------------------------------
Currency Converter
--------------------------------------------------
Approach:
- Used an exchange rate API (e.g., ExchangeRate API).
- Fetches real-time currency exchange rates.
- User enters amount, source currency, and target currency → program converts.

How to Run:
1. Run the script.
2. Enter amount, source currency code (e.g., USD), and target currency code (e.g., INR).
3. Program fetches live rates and shows the result.

Example Input/Output:
Input: 100 USD to INR
Output: 100 USD = 8320 INR

Challenges Faced:
- Handling network errors and API downtime.
- API key management.
- Ensuring currency codes are valid.
--------------------------------------------------


--------------------------------------------------
Simple Quiz Application
--------------------------------------------------
Approach:
- Stored quiz questions and answers in a JSON file.
- Program reads questions, asks the user, and accepts input.
- At the end, displays the score.

How to Run:
1. Run the script.
2. Answer the questions displayed one by one.
3. At the end, view your score.

Example Input/Output:
Q1: Capital of India?
Input: Delhi
Output: Correct!

Q2: 5 + 7 = ?
Input: 12
Output: Correct!

Final Score: 2/2

Challenges Faced:
- Designing flexible JSON format for questions.
- Validating user input (case sensitivity, spelling).
- Handling multiple question types.
--------------------------------------------------


--------------------------------------------------
News Headlines Fetcher
--------------------------------------------------
Approach:
- Used NewsAPI (or similar free API).
- Fetches the latest 5 headlines from selected category (e.g., Sports, Technology).
- Displays headlines neatly to the user.

How to Run:
1. Run the script.
2. Choose a category (default = general).
3. Program fetches and prints the latest 5 headlines.

Example Input/Output:
Input: Category → Technology
Output:
1. AI is changing the world of coding
2. New smartphone launched...
3. ...

Challenges Faced:
- Handling API authentication with keys.
- Limiting output to 5 headlines.
- Managing different categories.
--------------------------------------------------


--------------------------------------------------
Basic Expense Tracker with File Storage
--------------------------------------------------
Approach:
- Extended Week 1 Budget Tracker.
- All income and expenses stored in a CSV file.
- Reads CSV to calculate total income, total expenses, and net balance.

How to Run:
1. Run the script.
2. Enter income/expense details.
3. Program saves them in CSV file.
4. Use summary option to view totals.

Example Input/Output:
Input: Add Expense → 500 Food
Input: Add Income → 2000 Salary
Output:
Total Income = 2000
Total Expense = 500
Net Balance = 1500

Challenges Faced:
- Managing CSV formatting (commas, new lines).
- Avoiding duplication of records.
- Handling file not found errors.
--------------------------------------------------
