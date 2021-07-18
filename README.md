# FinancialCalculators_project
Interest occurs in almost all financial happenings, whether it be on a loan which ends up with you paying more to the bank, or on an investment which ends up with you earning more. There are two main types of interest, compound and simple interest. *Simple interest* is continually calculated on the initial amount invested and is only calculated once per year. This interest amount is then added to the amount that you initially invested (known as the principal amount). *Compound interest* is different in that the interest is calculated on the current total known as the accumulated amount.

This is a program that allows the user to calculate their interest on an investment or the amount that should be repaid on a home loan each month using compund or simple interest formula. This programme can be used by small financial companies for customers to have acces to two different financial calculators: an **investment** calculator and a **home loan repayment** calculator

## How it Works
The user should be allowed to choose which calculation they want to do, which is the first output that the user sees when the program runs. Then the user can enter either Bond or Investment as an input to indicate which calculator they want to access.
If the user selects *investment*, ask the user to input:
1. The amount of money that they are depositing.
1. The interest rate (as a percentage). Only the number of the interest rate should be entered e.g. The user should enter 8 and not 8%.
1. The number of years they plan on investing for.
1. Then ask the user to input whether they want “simple” or “compound” interest, and store this in a variable called interest. Depending on whether they typed “simple” or “compound”, output the appropriate amount that they will get after the given period at the interest rate. Then print out the answer

If the user selects *bond*, ask the user to input:
1. The present value of the house. E.g. 100000
1. The interest rate. E.g. 7
1. The number of months they plan to take to repay the bond. E.g. 120. Then Calculate how much money the user will have to repay each month and output the answer.
