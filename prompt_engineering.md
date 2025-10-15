For developers using agentic coding tools

grok-code-fast-1
 is a lightweight agentic model which is designed to excel as your pair-programmer inside most common coding tools. To optimize your experience, we present a few guidelines so that you can fly through your day-to-day coding tasks.

Provide the necessary context
Most coding tools will gather the necessary context for you on their own. However, it is oftentimes better to be specific by selecting the specific code you want to use as context. This allows
grok-code-fast-1
 to focus on your task and prevent unnecessary deviations. Try to specify relevant file paths, project structures, or dependencies and avoid providing irrelevant context.

No-context prompt to avoid
Make error handling better

Good prompt with specified context
My error codes are defined in @errors.ts, can you use that as reference to add proper error handling and error codes to @sql.ts where I am making queries

Set explicit goals and requirements
Clearly define your goals and the specific problem you want 
grok-code-fast-1
 to solve. Detailed and concrete queries can lead to better performance. Try to avoid vague or underspecified prompts, as they can result in suboptimal results.

Vague prompt to avoid
Create a food tracker

Good, detailed prompt
Create a food tracker which shows the breakdown of calorie consumption per day divided by different nutrients when I enter a food item. Make it such that I can see an overview as well as get high level trends.

Continually refine your prompts
grok-code-fast-1
 is a highly efficient model, delivering up to 4x the speed and 1/10th the cost of other leading agentic models. This enables you to test your complex ideas at an unprecedented speed and affordability. Even if the initial output isn’t perfect, we strongly suggest taking advantage of the uniquely rapid and cost-effective iteration to refine your query—using the suggestions above (e.g., adding more context) or by referencing the specific failures from the first attempt.

Good prompt example with refinement
The previous approach didn’t consider the IO heavy process which can block the main thread, we might want to run it in its own threadloop such that it does not block the event loop instead of just using the async lib version

Assign agentic tasks
We encourage users to try 
grok-code-fast-1
 for agentic-style tasks rather than one-shot queries. Our Grok 4 models are more suited for one-shot Q&A while 
grok-code-fast-1
 is your ideal companion for navigating large mountains of code with tools to deliver you precise answers.

A good way to think about this is:

grok-code-fast-1
 is great at working quickly and tirelessly to find you the answer or implement the required change.
Grok 4 is best for diving deep into complex concepts and tough debugging when you provide all the necessary context upfront.
