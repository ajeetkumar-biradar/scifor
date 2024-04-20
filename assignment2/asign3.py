# Teacher wants to conduct a quiz activity in her class. For that she is planning to group 4 students for each team among 60 students. She wants to know how many teams she can create among 60 students.Write a program to find the total number of teams that can be created among students by dividing total number of students to the number of students per team.Total number of student = 60 Number of students per team =4

total_students = 60
students_per_team = 4

total_teams = total_students // students_per_team

print("Total number of teams that can be created:", total_teams)