Feature: User wants to get data from a stock

Scenario: User gets current stock's price
  Given User is on terminal
  When he enters the stock's code
  Then the current price is displayed
