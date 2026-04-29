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

def venturecapitalequitysale(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Venture Capital</b></u><br>
    Capital Type: Equity Sale</center></p>
    <p><b><u>Introduction</u></b><br>
    Venture Capital Equity Sale refers to the process by which a startup or high-growth company raises capital by selling ownership shares to venture capital investors. {n} fits that definition. Unlike debt financing, equity sales do not require repayment but result in partial ownership dilution for founders and existing shareholders. Venture capital equity transactions are typically structured through preferred shares and governed under the Securities Act of 1933 in the United States. These transactions are regulated and supervised by the U.S. Securities and Exchange Commission when securities are issued.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. A venture capital equity sale involves issuing shares—commonly preferred stock—to venture investors in exchange for funding. These shares often carry special rights such as liquidation preference, anti-dilution protection, board representation, and voting rights. The funding is typically used for product development, market expansion, hiring, or scaling operations. Equity sales are conducted during funding rounds such as Seed, Series A, Series B, and later growth rounds.<br><br>
    2. Equity sales are best suited for startups and growth-stage companies with scalable business models and high growth potential. Technology firms, fintech startups, biotech companies, and SaaS platforms commonly rely on venture capital equity funding. Companies that do not have stable cash flows but possess strong innovation potential are ideal candidates for this type of financing.<br><br>
    3. Venture capital equity offerings are generally structured as private placements under exemptions provided by the Securities Act of 1933, particularly Regulation D. These offerings are typically limited to accredited investors. Although privately placed, companies must comply with disclosure requirements and investor qualification standards. If the company later becomes public, reporting obligations under the Securities Exchange Act of 1934 may apply.<br><br>
    4. Equity sales result in ownership dilution for founders and early shareholders. Venture investors may require significant control rights, including board seats and veto power over major decisions. There is also valuation risk, as companies may raise funds at lower valuations during market downturns. Additionally, future funding rounds may further dilute ownership if not structured carefully.<br><br>
    5. To secure venture capital equity financing, companies must present a strong business plan, scalable revenue model, competitive advantage, and experienced management team. Investors evaluate market opportunity, traction metrics, financial projections, and exit potential (such as IPO or acquisition). Transparent governance, realistic valuation, and clear growth strategy significantly increase the probability of successful equity fundraising.
    </p>
    <p><u><b>References</u></b><br>
    1. U.S. Securities and Exchange Commission. (2023). Private Placements and Regulation D. https://www.sec.gov/smallbusiness/exemptofferings/regd<br>
    2. Securities Act of 1933. https://www.sec.gov/about/laws/sa33.pdf<br>
    3. Securities Exchange Act of 1934. https://www.sec.gov/about/laws/sea34.pdf<br>
    4. National Venture Capital Association. (n.d.). https://nvca.org<br>
    5. Investopedia. (n.d.). Venture Capital Definition. https://www.investopedia.com/terms/v/venturecapital.asp
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    • Compliance with the Securities Act of 1933<br>
    • Regulation D Private Placement Exemption<br>
    • Accredited Investor Participation<br>
    • Corporate Authorization for Share Issuance<br>
    • Shareholder Agreement Compliance<br>
    • Disclosure of Investment Risks<br>
    • AML/KYC Verification
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    • Term Sheet<br>
    • Share Subscription Agreement<br>
    • Shareholders' Agreement<br>
    • Amended Certificate of Incorporation<br>
    • Capitalization Table<br>
    • Business Plan and Financial Projections<br>
    • Board and Shareholder Resolutions<br>
    • Risk Disclosure Statement<br>
    • Form D Filing (if applicable)
    </p>
    """)
    introduction =introduction.format(n=name)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def venturecapitalequitysalefaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Venture Capital<br>
    Equity Sale</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is an equity sale in venture capital?</u></b><br>
    • Answer: An equity sale occurs when a startup or growth-stage company sells ownership shares to venture capital investors in exchange for funding.
    </p>
    <p><u><b>2. How does an equity sale work?</u></b><br>
    • Answer: The company issues new shares or transfers existing shares to investors in return for capital used to support business growth and operations.
    </p>
    <p><u><b>3. Who typically participates in venture capital equity sales?</u></b><br>
    • Answer: Participants usually include venture capital firms, angel investors, institutional investors, and strategic corporate investors.
    </p>
    <p><u><b>4. What is the main purpose of an equity sale?</u></b><br>
    • Answer: The primary purpose is to raise growth capital without incurring repayment obligations like debt financing.
    </p>
    <p><u><b>5. Does an equity sale dilute ownership?</u></b><br>
    • Answer: Yes, issuing new shares reduces the ownership percentage of existing shareholders.
    </p>
    <p><u><b>6. How is company valuation determined during an equity sale?</u></b><br>
    • Answer: Valuation is determined through financial analysis, growth potential assessment, market comparisons, and negotiation between founders and investors.
    </p>
    <p><u><b>7. What rights do venture capital investors receive?</u></b><br>
    • Answer: Investors may receive voting rights, board representation, preferred shares, liquidation preferences, and anti-dilution protections.
    </p>
    <p><u><b>8. What is preferred equity in venture capital?</u></b><br>
    • Answer: Preferred equity gives investors priority over common shareholders in dividends and liquidation events.
    </p>
    <p><u><b>9. What stages commonly involve equity sales?</u></b><br>
    • Answer: Equity sales occur during funding rounds such as seed, Series A, Series B, and later growth stages.
    </p>
    <p><u><b>10. How is an equity sale different from debt financing?</u></b><br>
    • Answer: Equity sales transfer ownership and do not require repayment, while debt financing requires principal and interest payments without ownership transfer.
    </p>
    <p><u><b>11. What are the advantages of equity sale financing?</u></b><br>
    • Answer: Advantages include no fixed repayment obligations, access to strategic expertise, and long-term partnership support.
    </p>
    <p><u><b>12. What are the risks of equity sale financing?</u></b><br>
    • Answer: Risks include ownership dilution, reduced control for founders, and potential conflicts with investors.
    </p>
    <p><u><b>13. Can founders sell their personal shares in an equity sale?</u></b><br>
    • Answer: Yes, secondary equity sales allow founders or early investors to sell existing shares for liquidity.
    </p>
    <p><u><b>14. How do venture capital firms exit after an equity sale?</u></b><br>
    • Answer: Venture capital firms typically exit through IPOs, mergers and acquisitions, or secondary sales to other investors.
    </p>
    <p><u><b>15. When should a company consider an equity sale?</u></b><br>
    • Answer: A company should consider an equity sale when it requires significant growth capital and is willing to share ownership and strategic control in exchange for funding.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def venturecapitalequitysaletwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Venture Capital</b></u><br>
    Capital Type: Equity Sale</p></center>
    <p><b><u>1 – Stage of Development Assessment</u></b><br>
    Venture capital equity sales are best suited for: Early-stage startups (Seed / Pre-Series A); Growth-stage companies (Series A–C); High-growth, scalable businesses; Innovation-driven enterprises. Companies are typically pre-IPO and seeking rapid expansion capital.
    </p>
    <p><b><u>2 – Entity Type Assessment</u></b><br>
    Most appropriate for: C-Corporations (especially Delaware C-Corp in U.S. markets); High-growth startups; Technology, biotech, fintech, SaaS companies. VC investors generally avoid sole proprietorships or informal structures.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</u></b><br>
    Before raising VC equity, companies typically need: Strong business model; Scalable revenue strategy; Defined product-market fit; Cap table clarity; Pitch deck and financial projections; Founding team credibility. Due diligence focuses on growth potential and exit scalability.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</u></b><br>
    Venture equity sales occur in the private securities market, structured under exemptions regulated by the U.S. Securities and Exchange Commission (commonly Regulation D in the U.S.). Capital is raised from: Venture capital funds; Angel syndicates; Corporate venture arms; Institutional seed funds.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</u></b><br>
    Typical raise amounts vary by round: Seed: $250,000 – $2 million; Series A: $2 million – $15 million; Series B/C: $15 million – $100+ million. Amount depends on valuation and growth strategy.
    </p>
    <p><b><u>6 – Capital Round Assessment</u></b><br>
    Equity sale structures include: Preferred stock issuance; Participating preferred shares; Convertible preferred equity; Pro-rata investor rights; Board representation agreements. VC equity often includes liquidation preference and anti-dilution protections.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</u></b><br>
    Funding may be structured as: Single closing; Milestone-based tranches; Rolling close with multiple investors. Lead investors typically anchor the round.
    </p>
    <p><b><u>8 – Use of Funds Assessment</u></b><br>
    Common uses include: Product development; Market expansion; Hiring key talent; Marketing and customer acquisition; Infrastructure scaling. Capital is growth-focused rather than debt repayment.
    </p>
    <p><b><u>9 – Risk Assessment</u></b><br>
    Risk level: High. Risks include: Equity dilution; Loss of partial control; Board governance shifts; Exit pressure (IPO or acquisition expectations); High growth expectations. VC investors expect significant return multiples.
    </p>
    <p><b><u>10 – Capital Cost Assessment</u></b><br>
    Cost of capital is primarily: Ownership dilution; Preferred shareholder rights; Potential control concessions; Exit-driven growth expectations. There is no fixed interest, but long-term equity cost may be substantial.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</u></b><br>
    Upfront costs are moderate, including: Legal documentation; Cap table restructuring; Financial modeling; Advisory or placement support. Less expensive than IPO-level fundraising.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</u></b><br>
    Typical timeline: 1–4 months, depending on: Investor interest; Due diligence speed; Valuation negotiation; Market conditions. Highly network-driven and relationship-based process.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
