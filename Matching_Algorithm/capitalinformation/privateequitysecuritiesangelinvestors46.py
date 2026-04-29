from django.shortcuts import render,HttpResponse,redirect
from django.utils.safestring import mark_safe
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,\
EQuestions6,EQuestions7,EQuestions8,EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,EQuestions14,DocumentsPrepared
from iquestions.models import IQuestions1,IQuestions2
from registration.models import User,UserDetail,UserDetail2
from connections.models import Match_Data
from datetime import datetime
from django.contrib.auth.decorators import login_required
from ..models import Capital_Matches,Matches_Purchased,Letter_Response,Purchases

def privateequitysecuritiesangelinvestors(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Angel Investors </center></p>
    <p><b><u>Introduction</u></b><br>
    Angel Investors are ideal for very early-stage startups that need "seed" capital to move from a prototype or an idea to a functioning business with early market traction. They are designed so that high-net-worth individuals can use their personal wealth to back risky, high-potential ventures in exchange for equity or convertible debt. {n} fits that definition. In 2026, the angel market has evolved from solitary "lone wolf" checks into highly organized Angel Syndicates and digital communities. Platforms like AngelList and specialized groups (e.g., Hustle Fund's Angel Squad) allow individuals to pool resources, meaning a founder can raise a single $500,000 round from 50 different angels via a single line on the cap table. While individual checks typically range from $10,000 to $100,000, the aggregate value of the global angel market is projected to exceed $210 billion by 2033, driven by a massive influx of Gen Z and Millennial investors prioritizing ESG and "impact" alongside returns. While Angel Investors provide critical early oxygen and mentorship, the primary risks include significant equity dilution at a low valuation and the "informal" nature of the relationship—an unseasoned angel may become overly intrusive or, conversely, completely unresponsive when you need a follow-on introduction.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1. An Angel Investor is an "Accredited Investor" who provides capital for a business startup, usually in exchange for convertible debt or ownership equity. Unlike Venture Capitalists (VCs), who manage other people's money in a formal fund, angels invest their own personal capital. Because it is their own money, they are often more willing to take a "bet on the founder" before a product has proven revenue. (J.P. Morgan, 2024)<br>
    <br>2. The best type of companies to raise angel money are those in the Pre-Seed or Seed stages. Investors look for a large "Total Addressable Market" (TAM) and a founding team with a high "right to win." In 2026, angels are particularly aggressive in sectors like AI, Biotech, and ClimateTech, where the technical risk is high but the potential for a 100x return justifies the gamble. (SkyQuest, 2025)<br>
    <br>3. The term "Angel" originated from Broadway, where wealthy patrons funded theatrical productions to keep them from closing. In the 2026 financial landscape, angels have become the "First Institutional-ish" check. Modern regulations like Reg CF (Crowdfunding) have also allowed "Micro-Angels"—non-accredited individuals—to participate in rounds with as little as $1,000, further democratizing the capital pool. (MasterClass, 2026)<br>
    <br>4. While Angel capital is "patient," it carries "Governance and Dilution" risks. Many angels use SAFEs (Simple Agreement for Future Equity), which delay setting a valuation until a later VC round. If a founder raises too much via SAFEs at a low "Valuation Cap," they may find themselves owning less than 50% of their company before they even reach Series A. (Hustle Fund, 2026)<br>
    <br>5. To raise Angel capital, a founder typically starts with a Pitch Deck and a "Warm Intro." In 2026, the process is increasingly digital; founders often participate in "Demo Days" via Zoom or pitch to syndicates on investment platforms. The due diligence is generally "light" compared to VCs, focusing on the team's background, intellectual property (IP) ownership, and early proof of concept. (Sprintlaw, 2026)
    </p>
    <p><u><b>References</u></b><br>
    J.P. Morgan. (2024, Sept 12). Understanding Angel Financing and Investing. https://www.jpmorgan.com/insights/banking/commercial-banking/what-is-angel-financing<br>
    SkyQuest Technology. (2025). Global Angel Funds Market Size and Analysis 2025-2033. https://www.skyquestt.com/report/angel-funds-market<br>
    Hustle Fund. (2026). Angel Investing for Beginners: The Only Guide You Need. https://www.hustlefund.vc/post/angel-squad-angel-investing-for-beginners<br>
    Sprintlaw. (2026, Jan 12). Angel Investors: What They Look For and Startup Legal Documents. https://sprintlaw.co.uk/articles/angel-investors-what-they-look-for/<br>
    Stripe Resources. (2024). Angel Investors vs. Venture Capitalists: What Founders Need to Know. https://stripe.com/resources/more/angel-investors-vs-venture-capitalists
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Accredited Investor Status – Generally requires $200k+ annual income or $1M+ net worth (excluding primary residence).<br>
    · Reg CF / Reg A+ Compliance – If raising from non-accredited "micro-angels," specific SEC filing limits apply.<br>
    · Qualified Small Business Stock (QSBS) – Section 1202 status, which can allow angels to pay zero capital gains tax if the company is a C-Corp and held for 5 years.<br>
    · IP Assignment – All intellectual property must be legally assigned to the corporate entity, not the individual founder.<br>
    · Bad Actor Disclosures – Verification that founders have no relevant criminal history or regulatory bans.<br>
    · "Blue Sky" Filings – State-level notifications (like Form D) required in the states where the angels reside.
    </p>
    <p><b><u>Supporting Document List</u></b><br>
    · Pitch Deck – Visual narrative of the problem, solution, and market size.<br>
    · SAFE or Convertible Note – The legal instrument used to defer valuation.<br>
    · Cap Table – Showing pre- and post-investment ownership percentages.<br>
    · Shareholders' Agreement – Outlining voting rights and "Drag-along/Tag-along" provisions.<br>
    · IP Assignment Agreement – Proof that the business owns its code/designs.<br>
    · Founders' Agreement – Setting vesting schedules for the original team (usually a 4-year "cliff").<br>
    · Articles of Incorporation – Evidence of the legal entity (typically a Delaware C-Corp).
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request, 'detail.html', context)

def privateequitysecuritiesangelinvestorsfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Equity Securities<br>
    Angel Investors</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What are angel investors?</u></b><br>
    •Answer: Angel investors are high-net-worth individuals who provide early-stage capital to startups in exchange for equity or convertible securities.
    </p>
    <p><u><b>2. At what stage do angel investors typically invest?</u></b><br>
    •Answer: Angel investors usually invest at the idea, pre-seed, or seed stage when businesses are still developing products or validating markets.
    </p>
    <p><u><b>3. How much funding do angel investors usually provide?</u></b><br>
    •Answer: Angel investments typically range from $10,000 to $500,000, depending on the startup's needs and the investor's capacity.
    </p>
    <p><u><b>4. What do angel investors receive in return for their investment?</u></b><br>
    •Answer: Angel investors generally receive equity ownership, convertible notes, or SAFE agreements representing future equity.
    </p>
    <p><u><b>5. Do angel investors take an active role in the business?</u></b><br>
    •Answer: Many angel investors provide mentorship, strategic advice, and industry connections in addition to capital.
    </p>
    <p><u><b>6. How is angel investing different from venture capital?</u></b><br>
    •Answer: Angel investing involves personal funds and earlier-stage companies, while venture capital usually involves institutional funds and later-stage investments.
    </p>
    <p><u><b>7. What types of businesses attract angel investors?</u></b><br>
    •Answer: Angel investors often favor innovative, high-growth startups in technology, healthcare, fintech, consumer products, and scalable service industries.
    </p>
    <p><u><b>8. How quickly can funding from angel investors be secured?</u></b><br>
    •Answer: Funding timelines vary but can range from a few weeks to several months depending on due diligence and negotiations.
    </p>
    <p><u><b>9. Are angel investments risky?</u></b><br>
    •Answer: Yes, angel investing is high risk because many early-stage startups fail, but successful investments can generate significant returns.
    </p>
    <p><u><b>10. Can startups raise money from multiple angel investors?</u></b><br>
    •Answer: Yes, startups often form angel syndicates where multiple investors collectively fund a single company.
    </p>
    <p><u><b>11. Do angel investors require collateral?</u></b><br>
    •Answer: No, angel investments are equity-based and do not require collateral or asset pledges.
    </p>
    <p><u><b>12. Can a company raise additional funding after angel investment?</u></b><br>
    •Answer: Yes, angel funding often helps startups reach milestones needed to attract venture capital or other institutional investors.
    </p>
    <p><u><b>13. What are the benefits of angel investors beyond capital?</u></b><br>
    •Answer: Benefits include mentorship, credibility, networking opportunities, and access to future funding sources.
    </p>
    <p><u><b>14. Is there equity dilution when working with angel investors?</u></b><br>
    •Answer: Yes, founders typically give up a portion of ownership in exchange for angel investment.
    </p>
    <p><u><b>15. When should a startup consider angel investors?</u></b><br>
    •Answer: Startups should consider angel investors when they need early-stage funding, strategic guidance, and validation before scaling further.
    </p>
    """)
    context = {
        'introduction':introduction,
    }
    return render(request, 'detail.html', context)

def privateequitysecuritiesangelinvestorstwelve(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    entity = EQuestions2.objects.get(user=request.user).Selected_Option
    stage = EQuestions1.objects.get(user=request.user).Selected_Option
    preraise = EQuestions3.objects.get(user=request.user).Selected_Option
    premarket = EQuestions4.objects.get(user=request.user).Selected_Options
    raisegoal = EQuestions5.objects.get(user=request.user).Selected_Option
    useoffund = EQuestions7.objects.get(user=request.user).Selected_Options
    enterprisecost = EQuestions8.objects.get(user=request.user).Selected_Option2
    tranch = EQuestions6.objects.get(user=request.user).Selected_Option
    rounds = EQuestions6.objects.get(user=request.user).Selected_Options
    upfrontcost = EQuestions.objects.get(user=request.user).Selected_Option
    upfronttime = EQuestions.objects.get(user=request.user).Selected_Option2
    introduction = """
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Private Equity Securities</b></u><br>
    Capital Type: Angel Investors</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    Angel investors are best suited for pre-revenue to early-revenue startups, particularly during the idea, MVP, or early traction stages. Angels often invest before institutional venture capital. Your stage: {stage}
    </p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    C-Corps are the preferred entity type for angel investment, especially for high-growth startups. LLCs may be acceptable in some cases, but sole proprietorships and partnerships are generally less attractive due to equity and governance limitations. Your entity: {entity}
    </p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    Most angel investors prefer companies that have raised little to no prior institutional funding. Founder capital, friends-and-family money, or small grants are typically acceptable at this stage. Your prior capital: {preraise}
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    Angel investing occurs within the private early-stage equity market, often involving individual accredited investors or angel networks rather than formal investment funds. Your market type: {premarket}
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    Angel rounds typically range from $25,000 to $1,000,000, depending on valuation, traction, and investor syndication. Your goal: {raisegoal}
    </p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
    Angel investments usually occur during pre-seed or seed rounds, and may be structured as equity, SAFE, or convertible notes. Your round: {tranch}
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    Angel capital is commonly raised in a single round, though some angels may release funds in milestones or follow-on checks. Your tranches: {rounds}
    </p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    Funds are generally used for: Product development, Market validation, Initial hiring, Early marketing and operations. Restrictions are informal but focused on business growth rather than personal use. Your use: {useoffund}
    </p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    Risk is very high, as early-stage startups have a high failure rate. Angels accept this risk in exchange for potential high returns.
    </p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    The cost of capital is high due to equity dilution, but there are no required repayments. Angels may also add strategic value and mentorship. Your cost: {enterprisecost}
    </p>
    <p><b><u>11 - Up Front Cost Assessment</u></b><br>
    Upfront costs are low to moderate, including legal documentation, valuation discussions, and platform or syndication fees, if applicable. Your upfront cost: {upfrontcost}
    </p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    Timing to capital varies, typically 2–6 months, depending on investor outreach, due diligence, and deal structuring. Your timeline: {upfronttime}
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction': introduction,
    }
    return render(request, 'detail.html', context)