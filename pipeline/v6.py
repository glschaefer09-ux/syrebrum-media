"""Batch v6 (from 11/5): 7 value Shorts + 3 promos carrying the WATCHED5 viewer code.
Claims stay inside the shipped Small Business Pack (booking, confirmations, quotes->invoices with payment link,
overdue reminders, review requests, social drafts you approve, morning report)."""
import sys
from engine import Scene as Sc, render, HERE, CY, WH, OR, GR, B, XB, R
from content import tip

SY = "Sigh-ree-brum"
URL = ("syrebrum.com", XB, 96, CY)
FOOT = [URL, ("Free beta now", XB, 62, GR), ("Code WATCHED5", XB, 60, OR), ("5% off your first month", B, 52, OR)]
CTA_SAY = f"Software that works for you, tailored by you. Try the free beta at {SY} dot com. Code watched five takes five percent off your first month."

V6 = {
"tip-raise-prices": tip(
    "Scared to raise your prices? Here's how to do it without the drama.",
    "Scared to raise prices?", "Do it without the drama.", "id:50629",
    [("Give regular customers a heads-up, a few weeks before the new price starts.",
      "Give notice", ["A few weeks ahead", "In writing", "A clear start date"]),
     ("Give one honest reason, like materials or fuel costs going up. No long apology.",
      "Give one reason", ["Materials went up", "Fuel went up", "No long apology"])],
    "id:232538", "Notice and a reason. That's it.", "Notice and a reason.", "That's it.", "id:59138"),
"tip-no-shows": tip(
    "Tired of no-shows? One message the day before fixes a lot of them.",
    "Tired of no-shows?", "Try one message the day before.", "id:304045",
    [("The day before, send the time, the address, and what they need to have ready.",
      "Remind them", ["The time", "The address", "What to have ready"]),
     ("Ask them to reply yes to confirm. If they don't, call before you drive out.",
      "Ask them to confirm", ["Reply YES to confirm", "No reply? Call first", "Don't drive out blind"])],
    "id:202987", "Confirm first. Drive second.", "Confirm first.", "Drive second.", "id:154829"),
"tip-before-after": tip(
    "Take a before and after photo on every single job.",
    "Before and after photos.", "Every single job.", "id:85347",
    [("It's proof of the work you did, if there's ever a question later.",
      "It's your proof", ["What it looked like", "What you did", "A record if questions come up"]),
     ("And it's your best social media post. Just ask the customer first.",
      "It's your best post", ["Real work, real results", "Better than stock photos", "Ask the customer first"])],
    "id:4728", "Two photos. Every job.", "Two photos.", "Every job.", "id:85341"),
"tip-while-youre-here": tip(
    "'While you're here, can you just...' Here's how to handle it.",
    "“While you're here,", "can you just…”", "id:257093",
    [("Say yes, with a price. Extra work is extra pay, even if it's small.",
      "Say yes, with a price", ["Extra work = extra pay", "Even small jobs", "Say it up front"]),
     ("Write it down before you start, so the invoice isn't a surprise.",
      "Write it down first", ["Add it to the job", "Agree the price", "No surprise invoice"])],
    "id:232538", "Yes, and here's the price.", "Yes,", "and here's the price.", "id:50629"),
"tip-slow-season": tip(
    "Slow season coming? Your best leads are customers you already have.",
    "Slow season coming?", "Call customers you already have.", "id:1028",
    [("Pull up everyone you worked for last year. They already trust you.",
      "Start with last year", ["Last year's jobs", "They already know you", "No ad spend"]),
     ("Send a short note offering a check-up or a seasonal service. Keep it personal.",
      "Offer something simple", ["A check-up", "A seasonal service", "Keep it personal"])],
    "id:202987", "Old customers. New work.", "Old customers.", "New work.", "id:59138"),
"tip-google-profile": tip(
    "Customers look you up on Google before they call. Fix these three things.",
    "They Google you first.", "Fix these three things.", "id:44647",
    [("Correct hours and phone number. Real photos of your work. Not stock photos.",
      "Get the basics right", ["Correct hours", "Correct phone number", "Real photos of your work"]),
     ("And reply to every review, the good ones and the bad ones. Short and polite.",
      "Reply to every review", ["The good ones", "The bad ones", "Short and polite"])],
    "id:215751", "Your profile is your first impression.", "Your Google profile", "is your first impression.", "id:154829"),
"fun-quick-job": tip(
    "Things customers say that are never quick.",
    "Things customers say", "that are never quick:", "id:350124",
    [("It'll only take five minutes. Can you just ballpark it? While you're here...",
      "You've heard these", ["“It'll only take 5 minutes.”", "“Can you just ballpark it?”", "“While you're here…”"]),
     ("And the classic: my last guy did it cheaper.",
      "And the classic:", ["“My last guy did it cheaper.”"])],
    "id:61298", "Tag someone who's heard all of these.", "Tag someone", "who's heard all of these.", "id:142641"),
}


def promo(hv, h1, h2, qa, qb, fv, fh, chips, fv2, fh2, chips2):
    return [
        Sc(hv, "big", top=560, bg=qa, head=[(h1, XB, 92, CY), (h2, XB, 84, WH)]),
        Sc(f"{SY} runs the back office for your business, right on your own computer.", "big", top=620, bg=qb,
           head=[("Meet Syrebrum.", XB, 110, CY), ("Your back office, on your computer.", B, 64, WH)]),
        Sc(fv, "chips", top=420, bg=qa, head=[(fh, XB, 86, WH)], chips=chips),
        Sc(fv2, "chips", top=420, bg=qb, head=[(fh2, XB, 86, WH)], chips=chips2, col=GR),
        Sc("And nothing goes out without your okay.", "big", top=680, bg="id:142641",
           head=[("Nothing goes out", XB, 104, WH), ("without your OK.", XB, 104, OR)]),
        Sc(CTA_SAY, "big", top=400,
           head=[("Software that works for you.", XB, 80, WH), ("Tailored by you.", XB, 88, OR)],
           foot=FOOT, pad=1.8, nosub=True),
    ]


V6.update({
"promo-groomer": promo(
    "Dog groomers. Your hands are full of dog. Who's booking the next appointment?",
    "Dog groomers:", "Hands full of dog. Who's booking?", "id:240197", "id:148322",
    "Clients book online, any hour. It lands on your schedule, with the confirmation already written.",
    "Booked while you groom", ["Online booking, any hour", "Stops double-booking", "Confirmation written for you"],
    "After each visit, a review request is drafted, and your social posts are drafted for you to approve.",
    "Reviews and posts, drafted", ["Review requests", "Social posts drafted", "You approve them"]),
"promo-trainer": promo(
    "Personal trainers. You coach all day, then chase payments all night.",
    "Personal trainers:", "Coach all day. Chase payments all night?", "id:65163", "id:66999",
    "Clients book sessions online, and it stops double-booking before it happens.",
    "Sessions, booked", ["Online booking", "Stops double-booking", "Your hours, your rules"],
    "Invoices carry your payment link, and late payers get a polite reminder, drafted for you.",
    "Invoices + reminders", ["Invoices with your pay link", "Overdue reminders drafted", "You tap send"]),
"promo-every-business": promo(
    "If you run a small business, you're doing two jobs. The work, and the paperwork.",
    "Small business owner?", "You're doing two jobs.", "id:215751", "id:32246",
    "Online booking. Quotes from your own prices that turn into invoices with your payment link.",
    "It handles the busywork", ["Online booking", "Quotes become invoices", "Your payment link"],
    "Overdue reminders, review requests and social posts, all drafted. Plus one report every morning.",
    "Drafted for you", ["Overdue reminders", "Review requests & social posts", "One morning report"]),
})

if __name__ == "__main__":
    for key in (sys.argv[1:] or V6):
        render(key, V6[key], f"{HERE}/v6/syrebrum-{key}.mp4")
