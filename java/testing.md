# How to test final class
* ProcessBuilder
"You don't want to test, that ProcessBuilder and Process work, only that you can work with their output.
When you create an interface one trivial implementation (that can be inspected easily) delegates to ProcessBuilder and Process,
another implementation mocks this behaviour.
Later on you might even have another implementation that does what you need without starting another process."
