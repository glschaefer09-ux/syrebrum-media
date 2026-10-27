"""v10: one LinkedIn-first Short on 'every team has its own AI, nobody connects them'.
Claims stay inside what ships: several AIs (Claude, ChatGPT, Gemini, local) working as one team,
one shared memory and task board, the owner approves before anything goes out."""
import sys
from engine import Scene as Sc, render, HERE, CY, WH, OR, GR, B, XB, R

SY = "Sigh-ree-brum"
FOOT = [("syrebrum.com", XB, 96, CY), ("Free beta now", XB, 62, GR), ("Code WATCHED5", XB, 60, OR), ("5% off your first month", B, 52, OR)]

V10 = {
"promo-ai-team": [
    Sc("A hundred people. A hundred AI assistants. A hundred versions of what's going on.", "big", top=560, bg="id:215751",
       head=[("100 people.", XB, 96, WH), ("100 AI assistants.", XB, 92, CY), ("100 versions of the truth.", XB, 76, OR)]),
    Sc("Every team gets its own AI, and every one of them gets better at its own job.", "chips", top=420, bg="id:232538",
       head=[("Every team has its own AI", XB, 80, WH)], chips=["Sales", "Office", "Scheduling", "Billing"]),
    Sc("But who makes sure it all still adds up to one business?", "big", top=620, bg="id:304045",
       head=[("Who connects", XB, 100, WH), ("all of it?", XB, 100, OR)]),
    Sc(f"{SY} puts your AIs on one team. Claude, ChatGPT, Gemini, or a local model, all working from one shared memory and one task list.", "chips", top=420, bg="id:202987",
       head=[("One team. One memory.", XB, 84, WH)], chips=["Claude", "ChatGPT", "Gemini", "Local AI"], col=GR),
    Sc("They hand work to each other and keep each other current, so you stop being the one who connects every conversation.", "chips", top=420, bg="id:154829",
       head=[("You stop being the go-between", XB, 76, WH)], chips=["Shared task list", "Hand-offs between AIs", "Everyone sees the same facts"]),
    Sc("And nothing goes out without your okay.", "big", top=680, bg="id:142641",
       head=[("Nothing goes out", XB, 104, WH), ("without your OK.", XB, 104, OR)]),
    Sc(f"Software that works for you, tailored by you. Try the free beta at {SY} dot com. Code watched five takes five percent off your first month.", "big", top=400,
       head=[("Software that works for you.", XB, 80, WH), ("Tailored by you.", XB, 88, OR)], foot=FOOT, pad=1.8, nosub=True),
],
}

if __name__ == "__main__":
    for key in (sys.argv[1:] or V10):
        render(key, V10[key], f"{HERE}/v10/syrebrum-{key}.mp4")
