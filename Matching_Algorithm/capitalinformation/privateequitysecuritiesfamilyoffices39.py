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

def privateequitysecuritiesfamilyoffices(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Family Offices</center></p>
    <p><b><u>Introduction</u></b><br>
    Family Offices are ideal for established companies seeking long-term, "patient" capital with fewer of the rigid exit timelines typically found in traditional Venture Capital or Private Equity firms. They are designed so that the private wealth of ultra-high-net-worth (UHNW) families can be managed as a professional investment vehicle, often taking direct equity stakes in privately held businesses. {n} fits that definition. The Family Office sector has seen an explosion in growth as billionaire families increasingly bypass traditional funds to invest "direct." In 2026, there are an estimated 15,000+ family offices globally managing over $6 trillion in assets. Unlike institutional PE firms that must return capital to limited partners within 7–10 years, family offices can hold investments for decades, often prioritizing generational wealth preservation over quick flips. On average, family office direct investments range from $1 million to $50 million, though "club deals" between multiple families can exceed $100 million. While Family Offices offer unique flexibility and strategic "relational" value, their internal structures can be less transparent, and the decision-making process is often tied to the specific personal values or whims of the family patriarch or matriarch.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1. A Family Office is a private wealth management advisory firm that serves ultra-high-net-worth investors. They are generally categorized as Single Family Offices (SFOs), which manage the wealth of one family, or Multi-Family Offices (MFOs), which serve several. In the private equity space, they provide "Direct Investment," meaning they buy equity in a company directly rather than investing in a third-party fund. (Investopedia, 2026)<br>
    <br>2. The best type of companies to raise money from family offices are those with strong "cash-on-cash" returns and a clear alignment with the family's heritage or industry expertise. For example, a family that made their fortune in logistics will often be the best "smart money" partner for a tech startup in the supply chain space. They prefer companies with proven management teams that are beyond the "seed" stage and ready for scale. (Forbes, 2025)<br>
    <br>3. Family Offices emerged in the modern sense with the House of Morgan and the Rockefellers in the 19th century. However, the 2025-2026 landscape is defined by the "Direct Investing" trend. Families have realized that by investing directly, they avoid the "2-and-20" fee structure of PE funds and gain more control over their capital. This has turned family offices into major competitors for mid-market buyout deals once dominated by institutional firms. (Campden Wealth, 2025)<br>
    <br>4. While the "Patient Capital" is a benefit, it carries "idiosyncratic" risks. Because the capital belongs to a family, a change in family dynamics—such as a divorce, death, or internal dispute—can suddenly freeze investment decisions. Furthermore, family offices often have smaller teams than VCs, which can lead to a slower due diligence process and less operational support post-investment. (Wealth-X, 2026)<br>
    <br>5. To raise capital via a Family Office, a founder usually needs a "warm intro." Most family offices do not have public application portals and rely on a trusted network of lawyers, accountants, and other founders. The pitch must emphasize long-term sustainability and values alignment. Because they are "Qualified Purchasers" or "Accredited Investors," the legal paperwork is generally streamlined under Regulation D, but the "Subscription Agreement" remains a critical binding document. (Family Capital, 2025)
    </p>
    <p><u><b>References</u></b><br>
    · Investopedia. (2026, Jan 05). Family Office: What It Is, Types, and Services. https://www.investopedia.com/terms/f/family-office.asp<br>
    · Forbes. (2025, Sept 18). Why Family Offices Are Winning the Direct Investment War. https://www.forbes.com/family-offices/<br>
    · Campden Wealth. (2025). The Global Family Office Report 2025. https://www.campdenwealth.com/reports<br>
    · Wealth-X. (2026). Family Office Trends and Direct Investment Outlook. https://wealthx.com/intelligence/reports/<br>
    · Family Capital. (2025). Direct Investing for the Modern Family Office. https://www.famcap.com/
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Accredited Investor / Qualified Purchaser – The Family Office must meet SEC thresholds (typically $5M+ in investments for SFOs) to participate in private placements.<br>
    · Regulation D Compliance – Most deals are structured under Rule 506(b) or 506(c) to maintain privacy while raising capital.<br>
    · Investment Management Agreement (IMA) – If an external manager is making the decision for the family, this legal document must be in place.<br>
    · Know Your Customer (KYC) / AML – The business must perform due diligence on the "Source of Wealth" to comply with anti-money laundering regulations.<br>
    · State Blue Sky Laws – Notice filings must be made in the state where the family office is headquartered.<br>
    · Confidentiality / NDA – Given the high profile of these families, a strict Non-Disclosure Agreement is usually the first legal document signed.
    </p>
    <p><b><u>Supporting Document List</u></b><br>
    · Pitch Deck – Focused on long-term value and "the story" of the company.<br>
    · Detailed Financial Model – 5-year projections showing dividends or exit potential.<br>
    · Capitalization Table (Cap Table) – Showing existing ownership and the "dilution" the family will take.<br>
    · Shareholders' Agreement – Outlining the rights of the family (e.g., board seats, veto rights).<br>
    · Subscription Agreement – The legal contract for the purchase of the shares.<br>
    · Quality of Earnings (QofE) – For mid-market deals, a third-party audit of the cash flow.<br>
    · Governance Documents – Articles of Incorporation and Bylaws.
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesfamilyofficesfaq(request):
    introduction = """
    <p><b><center>Capital Market: Private Equity Securities<br>
    Family Offices</center></b></p>
    <p><center><u><b>Frequently Asked Questions</u></b></center></p>
    <p><u><b>1. What are family offices in private equity investing?</u></b><br>
        •Answer: Family offices are private wealth management entities that manage investments for high-net-worth families and deploy capital into private equity opportunities to achieve long-term wealth growth and diversification.
    </p>
    <p><u><b>2. What types of businesses typically attract family office investment?</u></b><br>
        •Answer: Family offices often invest in established or growth-stage businesses with strong fundamentals, sustainable cash flows, and long-term value creation potential.
    </p>
    <p><u><b>3. How much capital can family offices invest in a single deal?</u></b><br>
        •Answer: Investment sizes vary widely but typically range from several million dollars to tens or even hundreds of millions, depending on the family office's strategy.
    </p>
    <p><u><b>4. How quickly can funding be secured from a family office?</u></b><br>
        •Answer: Funding timelines are flexible and relationship-driven, often taking several weeks to months due to due diligence and alignment on long-term goals.
    </p>
    <p><u><b>5. Do family offices require equity ownership?</u></b><br>
        •Answer: Yes, family offices usually invest in exchange for equity ownership, although structures may include minority or majority stakes.
    </p>
    <p><u><b>6. What level of control do family offices seek?</u></b><br>
        •Answer: Control preferences vary; some family offices seek board seats or strategic influence, while others remain passive investors.
    </p>
    <p><u><b>7. What are the main advantages of family office investment?</u></b><br>
        •Answer: Advantages include patient capital, long-term investment horizons, flexible deal structures, and strategic mentorship from experienced investors.
    </p>
    <p><u><b>8. What risks are associated with family office funding?</u></b><br>
        •Answer: Risks include potential misalignment of vision, concentrated decision-making, and less formal exit timelines compared to institutional investors.
    </p>
    <p><u><b>9. Can startups receive funding from family offices?</u></b><br>
        •Answer: Yes, some family offices invest in startups, though many prefer later-stage or revenue-generating businesses with reduced risk.
    </p>
    <p><u><b>10. How do family offices differ from venture capital firms?</u></b><br>
        •Answer: Family offices invest their own capital, often take a long-term approach, and may prioritize stability and legacy over rapid exits.
    </p>
    <p><u><b>11. Can family office investments be combined with other funding sources?</u></b><br>
        •Answer: Yes, family office capital is often combined with venture capital, private equity funds, debt financing, or co-investments.
    </p>
    <p><u><b>12. What industries do family offices commonly invest in?</u></b><br>
        •Answer: Common industries include real estate, technology, healthcare, consumer goods, energy, and family-aligned sectors.
    </p>
    <p><u><b>13. Are there specific return expectations for family offices?</u></b><br>
        •Answer: Return expectations vary, but family offices generally seek steady, long-term returns rather than short-term speculative gains.
    </p>
    <p><u><b>14. What due diligence do family offices typically conduct?</u></b><br>
        •Answer: Due diligence often includes financial analysis, management assessment, market evaluation, and legal and operational reviews.
    </p>
    <p><u><b>15. How can a business attract investment from a family office?</u></b><br>
        •Answer: Businesses can attract family office investment by demonstrating strong governance, clear growth strategy, aligned values, and transparent financial reporting.
    </p>
    """
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesfamilyofficestwelve(request):
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
    Capital Type: Family Offices</p></center>
    <p><b><u>1 – Stage of Development Assessment</u></b><br>
    Family offices typically invest in growth-stage to mature companies, though some are open to late-seed or early-stage opportunities if there is a strong business model and credible management team. They often favor companies with clear scalability or long-term value creation potential. Stage: {stage}
    </p>
    <p><b><u>2 – Entity Type Assessment</u></b><br>
    The most suitable entity types are C-Corporations and LLCs, as these structures allow flexibility in equity ownership and governance. Family offices may also invest through holding companies or special purpose vehicles (SPVs) depending on the deal structure. Entity: {entity}
    </p>
    <p><b><u>3 – Pre-Capital Assessment</u></b><br>
    Family offices usually expect some operational traction, such as revenue generation, customer growth, or proven unit economics. While requirements are less rigid than institutional venture capital, businesses must demonstrate financial discipline and a clear growth strategy. Prior Raise: {preraise}
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</u></b><br>
    Investments occur in the private capital market, with terms negotiated directly between the family office and the company. Funding structures can include common equity, preferred equity, convertible instruments, or hybrid securities. Previous Market: {premarket}
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</u></b><br>
    Family offices can participate in small to large capital raises, often ranging from $500,000 to $50 million or more, depending on the family's wealth, risk appetite, and investment mandate. Raise Goal: {raisegoal}
    </p>
    <p><b><u>6 – Capital Round Assessment</u></b><br>
    Family offices commonly invest during Series A through Series C rounds, though some engage in seed or late-stage growth rounds. They may act as lead investors or co-invest alongside venture capital or private equity firms. Round Stage: {tranch}
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</u></b><br>
    Capital may be deployed in a single tranche or across multiple tranches tied to milestones, allowing family offices to manage risk while supporting long-term company growth. Rounds: {rounds}
    </p>
    <p><b><u>8 – Use of Funds Assessment</u></b><br>
    Funds are typically used for market expansion, product development, acquisitions, hiring key talent, and scaling operations. Family offices generally allow flexibility, provided the use aligns with agreed strategic objectives. Use of Funds: {useoffund}
    </p>
    <p><b><u>9 – Risk Assessment</u></b><br>
    Risk tolerance is moderate to high, as family offices often invest patient capital with longer time horizons. However, they still face risks related to execution, market volatility, and liquidity constraints.
    </p>
    <p><b><u>10 – Capital Cost Assessment</u></b><br>
    The cost of capital involves equity dilution and governance considerations. While family offices may accept lower returns than institutional investors, they often seek meaningful ownership stakes and strategic influence. Enterprise Cost: {enterprisecost}
    </p>
    <p><b><u>11 – Up Front Cost Assessment</u></b><br>
    Upfront costs are moderate, including legal, valuation, and due diligence expenses. There are typically no program fees, but transaction costs can be significant depending on deal complexity. Upfront Cost: {upfrontcost}
    </p>
    <p><b><u>12 – Timing to Capital Assessment</u></b><br>
    Timing to capital is moderate, usually 2–6 months, as family offices conduct thorough due diligence and often rely on relationship-based decision-making rather than formal investment committees. Upfront Time: {upfronttime}
    </p>
    """
    introduction = mark_safe(introduction.format(stage=stage,entity=entity,preraise=preraise,premarket=premarket,raisegoal=raisegoal,tranch=tranch,rounds=rounds,useoffund=useoffund,enterprisecost=enterprisecost,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)