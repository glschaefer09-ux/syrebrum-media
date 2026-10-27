"""Batch v9 (from 10/28, a third daily YouTube slot): 8 value Shorts. Tips only, soft brand outro,
no product claims inside the video and no phone number."""
import sys
from engine import render, HERE
from content import tip

V9 = {
"tip-on-my-way": tip(
    "Running to a job? Send one text before you get there.",
    "Heading to a job?", "Send one text first.", "texting on phone",
    [("Something like: hi, it's the tech from your service call, I'm on my way, about twenty minutes out.",
      "Say who and when", ["Who you are", "You're on the way", "About how long"]),
     ("Customers relax when they know you're coming, and they're ready when you knock.",
      "Why it works", ["No guessing", "They're home and ready", "Feels professional"])],
    "id:202987", "One text. Better first impression.", "One text.", "Better first impression.", "id:154829"),
"tip-quote-same-day": tip(
    "Want to win more jobs? Send the quote the same day you look at the job.",
    "Want to win more jobs?", "Quote the same day.", "id:232538",
    [("The customer is still thinking about the problem, and they're probably getting other quotes too.",
      "While it's fresh", ["Still thinking about it", "Comparing quotes", "Ready to decide"]),
     ("Even a simple quote today beats a perfect one next week.",
      "Fast beats perfect", ["Clear price", "What's included", "Sent today"])],
    "id:232538", "Look today. Quote today.", "Look today.", "Quote today.", "typing on laptop"),
"tip-check-in-after": tip(
    "Here's a simple habit that brings customers back: check in a week after the job.",
    "Job done last week?", "Check in.", "id:154835",
    [("A short message: just checking everything's still working well. Let me know if anything comes up.",
      "Keep it short", ["Everything still good?", "Here if you need me", "No sales pitch"]),
     ("It catches small problems early, and customers remember the business that checked.",
      "Why it works", ["Catches problems early", "Builds trust", "They call you next time"])],
    "id:154829", "One message builds real trust.", "One message.", "Real trust.", "woman reading phone smiling"),
"tip-holiday-hours": tip(
    "Holidays are coming. Update your hours on Google before customers show up to a locked door.",
    "Holidays coming?", "Update your Google hours.", "id:215751",
    [("Add special hours for every day you're closed or closing early. It takes two minutes.",
      "Set special hours", ["Days you're closed", "Early closing", "Two minutes"]),
     ("Then post a quick update with your holiday schedule, so customers can plan ahead.",
      "Tell them early", ["A short post", "Your holiday schedule", "Before the rush"])],
    "id:215751", "The right hours. No wasted trips.", "The right hours.", "No wasted trips.", "id:154829"),
"tip-faq-page": tip(
    "Answering the same questions all day? Put them on your website once.",
    "Same questions every day?", "Answer them once.", "customer service phone call",
    [("Write down the ten questions customers ask the most: prices, areas you cover, how long jobs take.",
      "List the top ten", ["Prices", "Areas you cover", "How long it takes"]),
     ("Put the answers on one page, and send the link when someone asks.",
      "One page, one link", ["Plain answers", "Easy to find", "Send the link"])],
    "id:232538", "Answer once. Save hours.", "Answer once.", "Save hours.", "browsing website laptop"),
"tip-referral-ask": tip(
    "Your happiest customer is your best salesperson. Make it easy for them.",
    "Happy customer?", "Make referrals easy.", "id:154835",
    [("When the job's done and they're happy, ask once: do you know anyone else who needs this done?",
      "Ask once", ["Right after the job", "When they're happy", "One simple question"]),
     ("Leave a card or send your link, so passing you along takes them two seconds.",
      "Make it easy", ["Leave a card", "Send your link", "Two seconds to share"])],
    "id:154829", "Happy customers. More customers.", "Happy customers.", "More customers.", "friends talking coffee"),
"tip-clear-invoice": tip(
    "Want invoices paid faster? Put these on every one.",
    "Want invoices paid faster?", "Put these on every one.", "id:4728",
    [("The job name and date, so they know exactly what it's for.",
      "What it's for", ["The job", "The date", "What was done"]),
     ("The total, the due date, and a link to pay right on it.",
      "How to pay", ["The total", "The due date", "A link to pay"])],
    "id:202987", "Clear invoice. Easier to pay.", "Clear invoice.", "Easier to pay.", "paying with phone"),
"fun-office-calls": tip(
    "Things the office hears every single day.",
    "Things the office hears", "every single day:", "id:350124",
    [("Is he on his way? Can he come today? My neighbor said you'd do it for less.",
      "Every. Single. Day.", ["“Is he on his way?”", "“Can he come today?”", "“My neighbor said…”"]),
     ("And the classic: I called earlier, did anybody get my message?",
      "And the classic:", ["“I called earlier…”", "“Did anybody get my message?”"])],
    "id:61298", "Tag the person who runs your office.", "Tag the person", "who runs your office.", "id:142641"),
}

if __name__ == "__main__":
    for key in (sys.argv[1:] or V9):
        render(key, V9[key], f"{HERE}/v9/syrebrum-{key}.mp4")
