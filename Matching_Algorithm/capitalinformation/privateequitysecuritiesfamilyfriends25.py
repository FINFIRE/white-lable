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

def privateequitysecuritiesfamilyfriends(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Family and Friends</center></p>
    <p><b><u>Introduction</u></b><br>
    Family & Friends (F&F) rounds are ideal for companies seeking initial seed capital to validate a concept, build a prototype, or fund early market entry. They are designed so that personal networks can provide the earliest form of external equity or debt, helping privately held startups bridge the gap between personal savings and institutional investment. {n} fits that definition. The "Friends and Family" round has been the traditional starting point for entrepreneurship for centuries. In 2025, it remains the most common source of early-stage capital; recent data suggests that F&F rounds collectively infuse over $60 billion annually into the global startup ecosystem. Iconic companies like Amazon, where Jeff Bezos's parents invested approximately $250,000 in 1995, demonstrate the potential long-term impact of this capital. On average, F&F rounds range from $10,000 to $150,000, offering founders high speed-to-capital and more flexible terms than traditional venture firms. While F&F capital offers a fast and accessible lifeline, the potential for permanent relationship strain, "zombie" cap tables with unsophisticated investors, and the lack of professional mentorship are critical risks founders must navigate.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1. Family & Friends Securities are equity or debt instruments issued to an entrepreneur's immediate personal network. These investments are typically "pre-seed" and are based more on personal trust and the founder's character than on audited financials or market traction. Unlike professional Private Equity, these investors are often "non-accredited," meaning they may not meet specific income or net worth thresholds, which necessitates careful adherence to securities law exemptions. (Fiveable, 2025)<br>
    <br>2. The best type of companies to raise money via F&F are those at the ideation or "Minimum Viable Product" (MVP) stage. These startups often lack the metrics required by Angel investors or VCs but have a founder with a strong personal track record and a community that believes in their vision. It is most effective for businesses with low initial capital requirements that can reach a significant milestone (like a first customer or patent filing) using a relatively small amount of "patient capital." (DLA Piper, 2025)<br>
    <br>3. F&F rounds emerged as a formalized "capital market" with the rise of modern securities regulations in the mid-20th century. While entrepreneurs have always borrowed from family, the 1982 adoption of Regulation D by the SEC provided a clear legal safe harbor (specifically Rule 506) for small businesses to raise money from non-accredited investors without a full public offering. This transformed "informal" help into a structured "round" of financing that professionalizes the early-stage startup lifecycle. (Shipshape VC, 2025)<br>
    <br>4. While F&F capital is flexible, it carries significant "emotional and legal" risks. Recent research from Harvard Business School (2025) suggests that founders who rely on family capital may become more risk-averse, fearing the loss of a relative's retirement savings, which can paradoxically slow growth. Legally, having too many unaccredited investors can "poison" a cap table, making it difficult to attract Series A VCs who may be wary of the potential for future litigation or the lack of investor sophisticatedness. (Forbes India, 2025)<br>
    <br>5. To raise capital via Family & Friends, a founder should treat the process with the same rigor as an institutional round. This involves creating a professional pitch deck, clearly disclosing all risks (including the high probability of total loss), and using standardized legal documents like a SAFE (Simple Agreement for Future Equity) or a Convertible Note. Success requires setting clear boundaries: investors should understand that their capital does not grant them a seat at the "Thanksgiving table" to discuss business operations. (Jordensky, 2025)
    </p>
    <p><u><b>References</u></b><br>
    Fiveable. (2025). Friends and Family Investments Definition - Entrepreneurship Key Terms. https://fiveable.me/key-terms/entrepreneurship/friends-family-investments<br>
    DLA Piper. (2025). Friends and Family Round vs. Angel Round. https://www.dlapiper.com/insights/publications/accelerate/funding-equity-debt/friends-and-family-round-vs-angel-round<br>
    Shipshape VC. (2025, September 01). Friends and Family Investors: Your First Source of Startup Capital. https://www.shipshape.vc/friends-and-family-investors-your-first-source-of-startup-capital/<br>
    Forbes India / Harvard Business School. (2025, December 18). A Growth Tip for Founders: Maybe Don't Accept Funds from Family. https://www.forbesindia.com/article/thought-leadership/harvard-business-school/a-growth-tip-for-founders-maybe-dont-accept-funds-from-family/2989554/1<br>
    Jordensky. (2025). The Complete Guide to Raising Funds from Friends and Family. https://www.jordensky.com/blog/guide-to-raising-funds-from-friends-and-family
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Securities Law Exemption – Typically raised under Rule 506(b) of Regulation D, which allows for an unlimited number of accredited investors and up to 35 non-accredited investors.<br>
    · Pre-existing Relationship – Founders must prove a "substantive, pre-existing relationship" to avoid being accused of "general solicitation" (illegal public advertising).<br>
    · Disclosure Requirements – If non-accredited investors are included, the founder must provide robust disclosure documents (similar to a Private Placement Memorandum).<br>
    · No General Solicitation – You cannot post about the "investment opportunity" on public social media or websites.<br>
    · Blue Sky Laws – Must comply with individual state securities filings (notice filings) where the investors reside.<br>
    · Bad Actor Disqualification – Founders and significant shareholders must not have "bad actor" disqualifying events (e.g., certain criminal convictions).<br>
    · Anti-Fraud Provisions – Regardless of exemptions, the founder is legally liable for any "misleading or deceptive" statements made during the raise.
    </p>
    <p><b><u>Supporting Document List</u></b><br>
    · Term Sheet – A simple summary of the deal structure (Equity, Convertible Note, or SAFE).<br>
    · Subscription Agreement – The legal contract where the investor agrees to buy the shares and acknowledges the risks.<br>
    · Risk Disclosure Document – A "worst-case scenario" list highlighting that the investor could lose 100% of their money.<br>
    · Cap Table – A current list of who owns what percentage of the company.<br>
    · Promissory Note – (If the investment is a loan) Outlining interest rates and repayment dates.<br>
    · Investor Questionnaire – Used to verify if the investor is "Accredited" or "Sophisticated."<br>
    · SEC Form D – A notice filing that must be submitted to the SEC within 15 days of the first sale of securities.
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesfamilyfriendsfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Equity Securities<br>
    Family and Friends</center></b></p>
    <p><center><u><b>Frequently Asked Questions</u></b></center></p>
    <p><u><b>1. What are Private Equity Securities from Family & Friends, and how do they differ from other funding options?</u></b><br>
        •Answer: Private Equity Securities from Family & Friends involve raising capital from close personal connections, such as relatives or friends, in exchange for equity in the business, providing early-stage funding without formal institutional involvement.
    </p>
    <p><u><b>2. What types of businesses are best suited for Family & Friends funding?</u></b><br>
        •Answer: Early-stage startups, small businesses, or businesses with a strong founding team and clear growth potential are ideal, particularly those that may not yet qualify for traditional bank loans or venture capital.
    </p>
    <p><u><b>3. How much funding can I typically raise from Family & Friends?</u></b><br>
        •Answer: Funding amounts vary widely but usually range from a few thousand dollars up to $100,000, depending on personal networks and the financial capacity of contributors.
    </p>
    <p><u><b>4. How quickly can I access funds from Family & Friends?</u></b><br>
        •Answer: Access is typically faster than institutional funding, often within days or weeks, depending on discussions and agreement on terms.
    </p>
    <p><u><b>5. What are the costs of raising capital from Family & Friends?</u></b><br>
        •Answer: Costs are generally equity dilution and the potential strain on personal relationships, rather than formal interest or fees, though legal and administrative costs may apply.
    </p>
    <p><u><b>6. Do I have to give up equity when raising funds from Family & Friends?</u></b><br>
        •Answer: Yes, capital is usually provided in exchange for a percentage of ownership, with the amount of equity negotiated based on investment size and valuation.
    </p>
    <p><u><b>7. Can I still raise capital from other sources while using Family & Friends funding?</u></b><br>
        •Answer: Yes, Family & Friends funding is often used as seed capital to demonstrate traction, making it easier to attract angel investors or venture capital later.
    </p>
    <p><u><b>8. What are the key benefits of Family & Friends funding over traditional investors?</u></b><br>
        •Answer: Benefits include quick access to funds, lower legal complexity, flexible terms, and supportive investors who may be more patient than formal venture capitalists.
    </p>
    <p><u><b>9. What resources and support can I expect from Family & Friends investors?</u></b><br>
        •Answer: Support is usually limited to advice or mentorship from experienced friends or family, rather than structured programs or professional guidance.
    </p>
    <p><u><b>10. What happens after Family & Friends investors provide funding?</u></b><br>
        •Answer: Investors become shareholders in your business, and it is important to maintain transparency, regular updates, and formal agreements to protect relationships and ensure clarity.
    </p>
    <p><u><b>11. Are there any risks associated with Family & Friends funding?</u></b><br>
        •Answer: Risks include relationship strain, potential disputes over equity, pressure to deliver results quickly, and personal liability if the business fails.
    </p>
    <p><u><b>12. How does Family & Friends funding compare to other private equity or debt options?</u></b><br>
        •Answer: It offers lower formal costs and quicker access compared to institutional private equity or bank loans, but may carry higher personal relationship risk and smaller funding amounts.
    </p>
    <p><u><b>13. Can I use Family & Friends funding if I have already raised other capital?</u></b><br>
        •Answer: Yes, but equity allocation and legal agreements must be carefully structured to avoid conflicts with other investors or dilution issues.
    </p>
    <p><u><b>14. What types of businesses typically benefit most from Family & Friends funding?</u></b><br>
        •Answer: Businesses in early product development, local services, small tech startups, or ventures with strong personal networks often benefit most.
    </p>
    <p><u><b>15. How can I increase my chances of successfully raising Family & Friends funding?</u></b><br>
        •Answer: Prepare a clear business plan, demonstrate traction, communicate equity terms transparently, formalize agreements legally, and maintain strong personal relationships.
    </p>
    """)
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesfamilyfriendstwelve(request):
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
    Capital Type: Family and Friends</p></center>
    <p><b><u>1 – Stage of Development Assessment</u></b><br>
    Family and friends' equity is best suited for idea-stage to early-growth startups, particularly when founders need quick, small-scale funding to develop prototypes, validate markets, or cover early operating expenses. Stage: {stage}
    </p>
    <p><b><u>2 – Entity Type Assessment</u></b><br>
    Eligible entities include C-Corps, LLCs, S-Corps, partnerships, and sole proprietorships. The key requirement is a formal structure to issue equity or document loans, ensuring clarity and legal compliance for both parties. Entity: {entity}
    </p>
    <p><b><u>3 – Pre-Capital Assessment</u></b><br>
    There are no restrictions on prior funding, though it is preferable to clearly communicate how existing or planned capital interacts with family and friends' investments. Prior Raise: {preraise}
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</u></b><br>
    This is non-market-based private financing. It does not involve banks, venture capital, or public investors. Previous funding sources generally do not affect eligibility. Previous Market: {premarket}
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</u></b><br>
    Capital raised through family and friends is typically small to moderate, depending on the personal network's resources and risk tolerance. Commonly ranges from a few thousand to tens of thousands of dollars. Raise Goal: {raisegoal}
    </p>
    <p><b><u>6 – Capital Round Assessment</u></b><br>
    This type of financing is usually pre-seed or seed stage, intended to help founders reach milestones that make the company attractive for formal investors or accelerators. Round Stage: {tranch}
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</u></b><br>
    Funds are typically provided in a single tranche, though multiple contributions can occur as milestones or needs arise. Agreements are informal but should ideally be documented. Rounds: {rounds}
    </p>
    <p><b><u>8 – Use of Funds Assessment</u></b><br>
    Funds can be used flexibly for:
    · Product development
    · Initial marketing and customer acquisition
    · Equipment or operational costs
    · Early hires
    Use of Funds: {useoffund}
    </p>
    <p><b><u>9 – Risk Assessment</u></b><br>
    Risk is high for both the founder and investors. The business may fail, potentially straining personal relationships. There is also legal and financial risk if terms are not properly documented.
    </p>
    <p><b><u>10 – Capital Cost Assessment</u></b><br>
    Cost of capital is equity dilution or agreed-upon repayment terms. Often, investors accept higher risk for potential upside, but founders must understand the impact on ownership. Enterprise Cost: {enterprisecost}
    </p>
    <p><b><u>11 – Up Front Cost Assessment</u></b><br>
    Upfront costs are low, typically limited to legal documentation or agreement preparation. No institutional fees or interest costs are involved unless agreed otherwise. Upfront Cost: {upfrontcost}
    </p>
    <p><b><u>12 – Timing to Capital Assessment</u></b><br>
    Access to funds is usually very fast, often within days to weeks, depending on investor readiness and paperwork completion. Upfront Time: {upfronttime}
    </p>
    """
    introduction = mark_safe(introduction.format(stage=stage,entity=entity,preraise=preraise,premarket=premarket,raisegoal=raisegoal,tranch=tranch,rounds=rounds,useoffund=useoffund,enterprisecost=enterprisecost,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)