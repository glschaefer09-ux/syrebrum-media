import json
B="https://raw.githubusercontent.com/glschaefer09-ux/syrebrum-media/1b68386b3d4647329102663068a43c5788a3ffdf/reels/v8/syrebrum-"
CODE="Viewer code WATCHED5 = 5% off your first month."
V=[
("2026-11-12","tip-invoice-same-day","Invoice the same day the job is done #Shorts",
 "Want to get paid faster? Send the invoice the same day the job is done, while it's fresh and the customer can see the work. Put the payment link right in the invoice so paying takes one tap.",
 "#Shorts #SmallBusinessTips #Contractor #CashFlow","Done today. Invoiced today. 🧾","When do you usually send your invoices? 👇",["invoicing","get paid faster","contractor tips","small business tips"]),
("2026-11-13","tip-reply-fast","New lead? Reply first #Shorts",
 "A new lead just messaged you. People often ask a few businesses at once, and the first one to reply often gets the job. Even a short reply works: thanks, I can help, when's a good time to take a look?",
 "#Shorts #SmallBusinessTips #Sales #Contractor","Reply first. Win more. ⚡","How fast do you usually reply to new leads? 👇",["lead response","sales tips","contractor tips","small business tips"]),
("2026-11-14","fun-estimate","Things customers say when they see the estimate #Shorts",
 "\"That's it? I could do that myself.\" \"My nephew has a truck.\" And the classic: \"Can you do it cheaper if I pay cash?\" Tag someone who's heard these.",
 "#Shorts #ContractorLife #TradesLife #SmallBusiness","😅","Which one have you heard the most? 👇",["contractor life","trades humor","estimates","small business"]),
("2026-11-15","tip-thank-you","The easiest marketing: say thank you #Shorts",
 "The easiest marketing there is: a short thank-you message after every job, using their name. Then, when they're happy, ask once: do you know anyone else who needs this done?",
 "#Shorts #SmallBusinessTips #Referrals #Marketing","Thank them. Then ask. 🙏","Do you ask happy customers for referrals? 👇",["referrals","customer thank you","small business marketing","small business tips"]),
("2026-11-16","tip-price-list","Write your price list down once #Shorts",
 "Still pricing every job from scratch? Write your price list down once: your common jobs, your materials and your labor rate. Quotes get faster, and every customer gets the same fair price.",
 "#Shorts #SmallBusinessTips #Pricing #Contractor","One list. Faster quotes. 📋","Do you keep a written price list? 👇",["price list","quoting","contractor tips","small business tips"]),
("2026-11-17","tip-busy-season","Book your regulars before the busy season #Shorts",
 "Your busy season is coming. Reach out to last year's customers now, while you still have open days. They get the day they want, and you get a calendar you can plan around.",
 "#Shorts #SmallBusinessTips #Scheduling #Contractor","Book early. Breathe later. 📅","When does your busy season start? 👇",["busy season","scheduling","repeat customers","small business tips"]),
("2026-11-18","tip-review-reply","How to reply to a bad review #Shorts",
 "Got a bad review? Thank them, say you're sorry it happened, and keep it short. Don't argue in public. Then offer to fix it and take the details offline.",
 "#Shorts #SmallBusinessTips #GoogleReviews #Reputation","Calm reply. Real fix. ⭐","How do you handle a bad review? 👇",["bad reviews","review replies","reputation management","small business tips"]),
]
P=[
("2026-11-13","promo-pool","Pool service: booked while you're on the route #Shorts",
 "Pool service owners: route full, inbox fuller? With Syrebrum, customers book online and it lands on your schedule with the confirmation already written. Invoices carry your payment link, and late payers get a polite reminder, drafted for you. Nothing goes out without your OK.",
 "#Shorts #PoolService #PoolCleaning #SmallBusiness","Share this with a pool pro 🏊","Tag a pool service owner 👇",["pool service","pool cleaning business","online booking","small business software","Syrebrum"]),
("2026-11-14","promo-caterer","Caterers: stop writing quotes all night #Shorts",
 "Caterers: every event starts with a quote, so why does it take all night? Syrebrum builds the quote from your own price list, and when they say yes it becomes the invoice with your payment link. After the event, review requests and social posts are drafted for you to approve. Nothing goes out without your OK.",
 "#Shorts #Catering #CateringBusiness #SmallBusiness","Share this with a caterer 🍽️","Tag a caterer 👇",["catering","catering business","quotes and invoices","small business software","Syrebrum"]),
("2026-11-15","promo-detailer","Car wash & detailing: booked while you work #Shorts",
 "Car wash and detailing owners: hands wet, who's booking the next car? With Syrebrum, customers book online any hour with no double-booking, and after each car a review request is drafted with your Google review link. You just hit send. Nothing goes out without your OK.",
 "#Shorts #CarDetailing #CarWash #SmallBusiness","Share this with a detailer 🚗","Tag a detailer 👇",["car detailing","car wash business","online booking","small business software","Syrebrum"]),
("2026-11-16","promo-spa","Spa & massage: booked while you work #Shorts",
 "Spa and massage owners: you can't answer the phone with oil on your hands. With Syrebrum, clients book online at any hour, it knows your hours and stops double-booking, and review requests are drafted after each visit. One morning report shows today's bookings. Nothing goes out without your OK.",
 "#Shorts #MassageTherapist #Spa #SmallBusiness","Share this with a spa owner 💆","Tag a massage therapist 👇",["massage therapist","spa business","online booking","small business software","Syrebrum"]),
]
out=[]
def add(date,time,key,yt,title,text,comment,tags):
    if yt:
        info={"autoPublish":True,"draft":True,"text":text,"firstCommentText":"","providers":[{"network":"youtube"}],"media":[B+key+".mp4"],
              "publicationDate":{"dateTime":f"{date}T{time}:00","timezone":"America/Chicago"},
              "youtubeData":{"title":title,"type":"short","privacy":"public","tags":tags,"category":"COMEDY" if key.startswith("fun") else "HOWTO_STYLE","madeForKids":False,"isAiGeneratedContent":True}}
    else:
        info={"autoPublish":True,"draft":True,"text":text,"firstCommentText":comment,"providers":[{"network":"facebook"},{"network":"instagram"}],"media":[B+key+".mp4"],
              "publicationDate":{"dateTime":f"{date}T{time}:00","timezone":"America/Chicago"},"videoCoverMilliseconds":1500,
              "facebookData":{"type":"REEL","title":title.replace(" #Shorts","")},
              "instagramData":{"type":"TRIAL_REEL" if key.startswith("fun") else "REEL","showReelOnFeed":True,"isAiGenerated":True}}
    out.append({"date":f"{date}T{time}:00-06:00","info":json.dumps(info,ensure_ascii=False)})
for d,k,t,body,h,tail,c,tags in V:
    add(d,"09:15",k,True,t,f"{body}\n\nFollow for a new tip every day.\n\nSyrebrum: software that works for you, tailored by you. https://www.syrebrum.com\n{CODE}\n\n{h}",c,tags)
    add(d,"19:32",k,False,t,f"{body}\n\n{tail} Follow for a new tip every day. Save this 📌\n\n{CODE} syrebrum.com\n\n{h.replace('#Shorts ','')} #Louisiana",c,tags)
for d,k,t,body,h,tail,c,tags in P:
    add(d,"16:05",k,True,t,f"{body}\n\nSoftware that works for you, tailored by you. Free beta: https://www.syrebrum.com · plans from $29.99/mo\n{CODE}\n\n{h}",c,tags)
    add(d,"11:35",k,False,t,f"{body}\n\nSoftware that works for you, tailored by you. Need something it doesn't do? Tell us.\n👉 Free beta at syrebrum.com · plans from $29.99/mo\n🎁 {CODE}\n\n{tail}\n\n{h.replace('#Shorts ','')} #Louisiana",c,tags)
import os
json.dump(out,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"schedule_v8.json"),"w"),ensure_ascii=False,indent=1)
print(len(out))
