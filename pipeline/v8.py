"""Batch v8 (from 11/12): 7 value Shorts + 4 promos. No phone number (no inbox yet). WATCHED5 on promo end cards.
Claims stay inside the shipped Small Business Pack (booking + confirmations, stops double-booking, quotes from your
price list -> invoice with your payment link, overdue reminders, review requests, social drafts you approve,
one morning report). Nothing goes out without the owner's OK."""
import sys
from engine import Scene as Sc, render, HERE, CY, WH, OR, GR, B, XB, R
from content import tip
from v6 import promo

V8 = {
"tip-invoice-same-day": tip(
    "Want to get paid faster? Send the invoice the same day the job is done.",
    "Want to get paid faster?", "Invoice the same day.", "id:4728",
    [("The job is fresh, the customer is happy, and the work is right in front of them.",
      "While it's fresh", ["The job just got done", "The customer is happy", "They can see the work"]),
     ("Put the payment link right in the invoice, so paying takes one tap.",
      "Make it one tap", ["Clear total", "What it was for", "A link to pay"])],
    "id:202987", "Done today. Invoiced today.", "Done today.", "Invoiced today.", "id:50622"),
"tip-reply-fast": tip(
    "A new lead just messaged you. The first business to reply often gets the job.",
    "A new lead messaged you.", "Reply first.", "id:304045",
    [("People ask a few businesses at once. A quick reply shows you're on it.",
      "They asked around", ["You're not the only one", "Speed shows you care", "Even a short reply"]),
     ("Something like: thanks, I can help. When's a good time to take a look?",
      "Keep it simple", ["Thanks for reaching out", "I can help", "When's a good time?"])],
    "id:202987", "Reply first. Win more.", "Reply first.", "Win more.", "id:154829"),
"tip-thank-you": tip(
    "The easiest marketing there is: a thank-you message after every job.",
    "The easiest marketing:", "Say thank you.", "id:154829",
    [("A short thank-you after the job makes you the business they remember.",
      "They remember you", ["After every job", "Short and personal", "Use their name"]),
     ("And when they're happy, ask: do you know anyone else who needs this done?",
      "Then ask once", ["Know anyone else?", "One simple question", "No pressure"])],
    "id:154835", "Thank them. Then ask.", "Thank them.", "Then ask.", "id:59138"),
"tip-price-list": tip(
    "Still pricing every job from scratch? Write your price list down once.",
    "Pricing every job from scratch?", "Write it down once.", "id:50629",
    [("Your common jobs, your materials, and your labor rate. All in one place.",
      "One list", ["Common jobs", "Materials", "Your labor rate"]),
     ("Quotes get faster, and every customer gets the same fair price.",
      "Then quote faster", ["Faster quotes", "Same price for everyone", "Fewer mistakes"])],
    "id:232538", "One list. Faster quotes.", "One list.", "Faster quotes.", "id:59138"),
"tip-busy-season": tip(
    "Your busy season is coming. Book your regulars before it hits.",
    "Busy season coming?", "Book your regulars now.", "id:1028",
    [("Reach out to last year's customers now, while you still have open days.",
      "Fill the calendar early", ["Last year's customers", "While you have open days", "Before the rush"]),
     ("They get the day they want, and you get a calendar you can plan around.",
      "Everyone wins", ["They pick the day", "You plan ahead", "Fewer emergencies"])],
    "id:202987", "Book early. Breathe later.", "Book early.", "Breathe later.", "id:59138"),
"tip-review-reply": tip(
    "Got a bad review? Here's how to reply without making it worse.",
    "Got a bad review?", "Reply like this.", "id:44647",
    [("Thank them, say you're sorry it happened, and keep it short. Don't argue in public.",
      "Stay calm", ["Thank them", "Say sorry it happened", "Don't argue"]),
     ("Then offer to fix it, and take the details offline.",
      "Offer to fix it", ["Offer a fix", "Give a way to reach you", "Take it offline"])],
    "id:215751", "Calm reply. Real fix.", "Calm reply.", "Real fix.", "id:154829"),
"fun-estimate": tip(
    "Things customers say when they see the estimate.",
    "Things customers say", "when they see the estimate:", "id:350124",
    [("That's it? I could do that myself. My nephew has a truck.",
      "Every. Single. Time.", ["“I could do that myself.”", "“My nephew has a truck.”", "“That's it?”"]),
     ("And the classic: can you do it cheaper if I pay cash?",
      "And the classic:", ["“Cheaper if I pay cash?”"])],
    "id:61298", "Tag someone who's heard these.", "Tag someone", "who's heard these.", "id:142641"),
"promo-pool": promo(
    "Pool service owners. Your route is full, and your inbox is fuller.",
    "Pool service owners:", "Route full. Inbox fuller.", "id:25000", "id:122892",
    "Customers book online, and it lands on your schedule with the confirmation already written.",
    "Booked while you're on the route", ["Online booking", "Stops double-booking", "Confirmation written for you"],
    "Invoices carry your payment link, and late payers get a polite reminder, drafted for you.",
    "Invoices + reminders", ["Your payment link", "Reminders at 3, 7, 14 days", "You tap send"]),
"promo-caterer": promo(
    "Caterers. Every event starts with a quote. Why does that take all night?",
    "Caterers:", "Why do quotes take all night?", "id:197205", "id:11606",
    "Build the quote from your own price list. When they say yes, it becomes the invoice with your payment link.",
    "Quote → Invoice → Payment link", ["From your own prices", "Yes becomes the invoice", "Your Stripe or Square link"],
    "After the event, a review request is drafted for you, and your social posts are drafted for you to approve.",
    "Reviews and posts, drafted", ["Review requests", "Social posts drafted", "You approve them"]),
"promo-detailer": promo(
    "Car wash and detailing owners. Your hands are wet. Who's booking the next car?",
    "Car wash & detailing:", "Hands wet. Who's booking?", "id:3555", "id:5644",
    "Customers book online any hour, and it lands on your schedule with no double-booking.",
    "Booked while you work", ["Online booking, any hour", "Stops double-booking", "Confirmation written for you"],
    "After each car, a review request is drafted with your Google review link. You just hit send.",
    "More reviews, less effort", ["Drafted after each car", "Your Google review link", "You hit send"]),
"promo-spa": promo(
    "Spa and massage owners. You can't answer the phone with oil on your hands.",
    "Spa & massage owners:", "Oil on your hands. Phone ringing.", "id:701", "id:204214",
    "Clients book online at any hour. It knows your rooms and your hours, and it stops double-booking.",
    "Booked while you work", ["Online booking", "Your rooms and hours", "Stops double-booking"],
    "After each visit, a review request is drafted, and your morning report shows what's booked today.",
    "Reviews and your day, handled", ["Review requests drafted", "Today's bookings", "One morning report"]),
}

if __name__ == "__main__":
    for key in (sys.argv[1:] or V8):
        render(key, V8[key], f"{HERE}/v8/syrebrum-{key}.mp4")
