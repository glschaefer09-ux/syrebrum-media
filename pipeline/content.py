"""Value Shorts for trade and small-business owners: money tips and relatable moments. Soft brand outro only."""
import sys
from engine import Scene as Sc, render, HERE, CY, WH, OR, GR, B, XB, R

OUT_FOOT = [("Follow for a tip every day", XB, 66, GR), ("syrebrum.com", XB, 84, CY)]
OUT_SAY = "Follow for a new tip every day."

def tip(hook_say, hook1, hook2, bg1, points, bg2, payoff_say, payoff1, payoff2, bg3):
    """points: list of (say, head, chips)"""
    sc = [Sc(hook_say, "big", top=560, bg=bg1, head=[(hook1, XB, 90, CY), (hook2, XB, 84, WH)])]
    for say, head, chips in points:
        sc.append(Sc(say, "chips", top=440, bg=bg2, head=[(head, XB, 84, WH)], chips=chips))
    sc.append(Sc(payoff_say, "big", top=640, bg=bg3, head=[(payoff1, XB, 96, WH), (payoff2, XB, 96, OR)]))
    sc.append(Sc(OUT_SAY, "big", top=640, head=[("Run the business. Not the paperwork.", XB, 80, WH)], foot=OUT_FOOT, pad=1.4, nosub=True))
    return sc

CONTENT = {
"tip-late-invoice": tip(
    "Stop texting late payers 'just checking in.' Here's what actually gets you paid.",
    "Late invoice?", "Stop saying 'just checking in.'", "id:202987",
    [("Say exactly what's owed, for which job, and put the pay link right in the message.",
      "Be specific", ["The job name", "The amount owed", "The link to pay"]),
     ("Send it at three days, again at seven, and again at fourteen. Same polite tone every time.",
      "Then repeat it", ["Day 3", "Day 7", "Day 14"])],
    "id:232538", "Clear and polite makes it easy to pay.", "Clear and polite", "makes it easy to pay.", "id:50622"),
"tip-good-better-best": tip(
    "Giving one price on every quote? You're leaving money on the table.",
    "One price per quote?", "You're leaving money on the table.", "id:50629",
    [("Give three options instead: good, better and best.",
      "Give three options", ["Good", "Better", "Best"]),
     ("Make each option different in what it includes. Customers like choosing, and not everyone wants the cheapest.",
      "Let them choose", ["Different scope, not just price", "Choosing feels fair", "Not everyone picks the cheapest"])],
    "id:232538", "Same job. Three options. Let them choose.", "Same job. Three options.", "Let them choose.", "id:59138"),
"tip-missed-call": tip(
    "You missed a call on the job. Here's how not to lose that customer.",
    "Missed a call on a job?", "Don't lose that customer.", "id:304045",
    [("A lot of people just call the next number on the list. So text back fast, even if you can't talk.",
      "Text back fast", ["Within minutes", "Even if you can't talk", "Before they call the next guy"]),
     ("Something like: sorry I missed you, I'm on a job. What do you need, and when's good to call?",
      "Keep it simple", ["Sorry I missed you", "I'm on a job", "When's good to call?"])],
    "id:202987", "A quick reply keeps the job in play.", "A quick reply", "keeps the job in play.", "id:154829"),
"tip-review-same-day": tip(
    "Want more reviews? Ask on the same day.",
    "Want more reviews?", "Ask on the same day.", "id:154829",
    [("Customers are happiest right when the job's done. That's the moment to ask.",
      "Timing is everything", ["Right after the job", "While they're happy", "Not next week"]),
     ("Ask every customer for an honest review, and send the direct link, not 'leave us a review sometime.'",
      "Send the link", ["Ask every customer", "An honest review", "The direct review link"])],
    "id:154835", "Same-day ask. Direct link.", "Same-day ask.", "Direct link.", "id:154829"),
"tip-deposit": tip(
    "Still starting big jobs with no deposit? Here's why that's costing you.",
    "No deposit on big jobs?", "It's costing you.", "id:50629",
    [("A clearly agreed deposit can help cover your materials, so you're not floating the job on your own card.",
      "Cover your materials", ["Helps cover materials", "Not on your card", "Less cash stress"]),
     ("Put the deposit terms in writing on the quote, so everyone knows what it covers.",
      "Put it in writing", ["Amount agreed up front", "Terms on the quote", "No surprises"])],
    "id:50622", "Big job? Agree a deposit.", "Big job?", "Agree a deposit.", "id:59138"),
"tip-quote-followup": tip(
    "Sent a quote and never heard back? Do this.",
    "Quote sent. Silence.", "Now what?", "id:232538",
    [("Follow up in two days with one short question: do you have any questions about the quote?",
      "Follow up in 2 days", ["One short message", "Ask if they have questions", "No pressure"]),
     ("Then once more, a week later. Still friendly. Then let it go.",
      "Then once more", ["One week later", "Still friendly", "Then let it go"])],
    "id:1028", "A polite follow-up keeps the door open.", "A polite follow-up", "keeps the door open.", "id:50629"),
"fun-hvac-july": tip(
    "Things every H V A C tech hears in July.",
    "Things every HVAC tech", "hears in July:", "id:61298",
    [("It was working yesterday. Can you just look at it real quick? My cousin said it's the Freon.",
      "Every. Single. Day.", ["“It was working yesterday.”", "“Just look at it real quick?”", "“My cousin said it's the Freon.”"]),
     ("And the classic: how much just to come out?",
      "And the classic:", ["“How much just to come out?”"])],
    "id:304045", "Tag a tech who's heard all of these.", "Tag a tech", "who's heard all of these.", "id:142641"),
"fun-diy-plumbing": tip(
    "Plumbers know this one. 'I already tried to fix it myself.'",
    "Plumbers know this one:", "“I already tried to fix it myself.”", "id:257093",
    [("It was only a little drip. I just used some tape. Then I watched a video.",
      "What they say", ["“It was only a little drip.”", "“I just used some tape.”", "“Then I watched a video.”"]),
     ("What you find: three kinds of tape, a new leak, and a bucket that's been there since March.",
      "What you find", ["Three kinds of tape", "A brand new leak", "A bucket from March"])],
    "id:350124", "Tag a plumber who's seen it.", "Tag a plumber", "who's seen it.", "id:257093"),
"fun-9pm-owner": tip(
    "Small business owner at nine p.m.",
    "Small business owner", "at 9 pm:", "id:215751",
    [("Answering texts. Writing tomorrow's quotes. Chasing last month's invoice.",
      "Still working", ["Answering texts", "Writing quotes", "Chasing invoices"]),
     ("And the email that says, quick question.",
      "And then…", ["“Quick question…”"])],
    "id:44647", "If this is you, there's a better way.", "If this is you,", "there's a better way.", "id:215751"),
}

if __name__ == "__main__":
    for key in (sys.argv[1:] or CONTENT):
        render(key, CONTENT[key], f"{HERE}/syrebrum-{key}.mp4")
