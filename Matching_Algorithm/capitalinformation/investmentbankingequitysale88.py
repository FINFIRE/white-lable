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

def investmentbankingequitysale(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Investment Banking</b></u><br>
    Capital Type: Equity Sale </center></p>
    <p><b><u>Introduction</u></b><br>
    An equity sale in investment banking refers to the structured offering and sale of ownership shares in a company to investors in exchange for capital. {n} fits that definition. Through an equity sale, a company raises funds by issuing common stock, preferred stock, or other equity instruments, typically facilitated by an investment bank or registered broker-dealer. Equity sales may occur privately under exemptions such as Regulation D or publicly through registered offerings. In the United States, equity offerings are governed by the Securities Act of 1933 and regulated by the U.S. Securities and Exchange Commission. Equity financing enables companies to secure substantial capital without repayment obligations, though it results in ownership dilution and shared governance.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. An equity sale involves issuing ownership interests in a company in exchange for capital contributions from investors. Securities may include common shares, preferred shares, or convertible equity instruments. Investment banks structure and distribute equity offerings to institutional and accredited investors. Equity sales can take place in private placements, venture rounds, growth equity transactions, or public offerings such as IPOs. Investors typically receive voting rights, economic participation, and potential dividend rights depending on share class.<br><br>
    2. Equity sales are best suited for high-growth companies seeking expansion capital without increasing debt leverage. Startups in technology, biotech, fintech, and scalable industries frequently rely on equity financing to fund R&D, acquisitions, and market expansion. Companies with strong revenue growth and defensible market positioning attract institutional equity investors.<br><br>
    3. The modern U.S. equity capital framework was established through the Securities Act of 1933 and the Securities Exchange Act of 1934, enacted after the 1929 stock market crash to enhance transparency and investor protection. These laws require disclosure of material information and regulate securities issuance, trading, and reporting obligations under SEC oversight.<br><br>
    4. While equity sales provide non-repayable capital, they dilute founder ownership and may reduce decision-making control. Investors often negotiate protective provisions such as board seats, liquidation preferences, anti-dilution clauses, and dividend rights. Public offerings require ongoing reporting compliance, increased scrutiny, and exposure to market volatility.<br><br>
    5. To conduct an equity sale, a company must prepare offering documentation, financial statements, capitalization tables, and governance disclosures. Investment banks conduct due diligence and assist in valuation and pricing strategy. Success depends on financial transparency, scalable business models, strong management teams, and regulatory readiness. Required filings may include Form D for private placements or Form S-1 for public offerings.
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    • Compliance with the Securities Act of 1933<br>
    • SEC Registration or Applicable Exemption (Reg D, Reg A+, etc.)<br>
    • Proper Disclosure of Material Information<br>
    • Corporate Authorization to Issue Shares<br>
    • Shareholder Approval (if required)<br>
    • AML/KYC Compliance<br>
    • Engagement with Registered Broker-Dealer (if transaction-based compensation applies)
    </p>
    <p><u><b>References</u></b><br>
    1. U.S. Securities and Exchange Commission. (2023). Securities Act of 1933 Overview. https://www.sec.gov/about/laws/sa33.pdf<br>
    2. Securities Exchange Act of 1934. (1934). U.S. Congress. https://www.sec.gov/about/laws/sea34.pdf<br>
    3. U.S. Securities and Exchange Commission. Form S-1 Registration Statement Guide. https://www.sec.gov/forms/s-1<br>
    4. Harvard Law School Forum on Corporate Governance. (2021). Equity Capital Markets and Corporate Governance. https://corpgov.law.harvard.edu<br>
    5. Investopedia. (n.d.). Equity Financing Definition. https://www.investopedia.com/terms/e/equityfinancing.asp
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    • Private Placement Memorandum (PPM) or Prospectus<br>
    • Subscription Agreement<br>
    • Share Purchase Agreement<br>
    • Corporate Formation Documents<br>
    • Amended & Restated Articles (if issuing new share class)<br>
    • Capitalization Table<br>
    • Financial Statements (Audited if required)<br>
    • Investor Pitch Deck<br>
    • Regulatory Filings (Form D, Form S-1, etc.)
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def investmentbankingequitysalefaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Investment Banking <br>
    Equity Sale</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is an equity sale in investment banking?</u></b><br>
    • Answer: An equity sale is the process of selling ownership shares of a company to investors to raise capital.
    </p>
    <p><u><b>2. Who typically manages an equity sale?</u></b><br>
    • Answer: Investment banks or licensed broker-dealers typically manage equity sales on behalf of the issuing company.
    </p>
    <p><u><b>3. What types of equity can be sold?</u></b><br>
    • Answer: Companies may sell common stock, preferred stock, or other equity-linked securities.
    </p>
    <p><u><b>4. Is an equity sale public or private?</u></b><br>
    • Answer: An equity sale can be conducted privately through private placements or publicly through an IPO or secondary offering.
    </p>
    <p><u><b>5. How is company valuation determined in an equity sale?</u></b><br>
    • Answer: Valuation is determined through financial analysis, comparable company benchmarks, market conditions, and investor demand.
    </p>
    <p><u><b>6. What are the benefits of an equity sale?</u></b><br>
    • Answer: Benefits include raising capital without repayment obligations and strengthening the company's balance sheet.
    </p>
    <p><u><b>7. What is dilution in an equity sale?</u></b><br>
    • Answer: Dilution occurs when new shares are issued, reducing the ownership percentage of existing shareholders.
    </p>
    <p><u><b>8. How are investors sourced in an equity sale?</u></b><br>
    • Answer: Investment banks market the offering to institutional investors, accredited investors, or public markets depending on the structure.
    </p>
    <p><u><b>9. What documents are required in an equity sale?</u></b><br>
    • Answer: Required documents may include offering memoranda, subscription agreements, financial disclosures, and regulatory filings.
    </p>
    <p><u><b>10. How long does an equity sale process take?</u></b><br>
    • Answer: The timeline varies but may range from a few months for private offerings to longer periods for public offerings.
    </p>
    <p><u><b>11. What fees are associated with an equity sale?</u></b><br>
    • Answer: Fees typically include underwriting fees, legal costs, accounting fees, and advisory compensation.
    </p>
    <p><u><b>12. Does an equity sale impact company control?</u></b><br>
    • Answer: Yes, issuing equity may affect voting rights and control depending on the percentage sold and share structure.
    </p>
    <p><u><b>13. What is the role of due diligence in an equity sale?</u></b><br>
    • Answer: Due diligence ensures accurate disclosure, assesses company risks, and supports investor confidence.
    </p>
    <p><u><b>14. Can equity sales be staged over time?</u></b><br>
    • Answer: Yes, companies may conduct multiple rounds of equity financing as they grow.
    </p>
    <p><u><b>15. When should a company consider an equity sale?</u></b><br>
    • Answer: A company should consider an equity sale when it needs growth capital, expansion funding, or strategic investors without increasing debt obligations.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def investmentbankingequitysaletwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Investment Banking</b></u><br>
    Equity Sale</p></center>
    <p><b><u>1 – Stage of Development Assessment</u></b><br>
    An investment banking-led equity sale is best suited for growth-stage to mature companies that: Have consistent revenue; Show scalable growth potential; Possess institutional-grade financial reporting; Are seeking significant expansion capital. Early-stage startups typically pursue venture capital before engaging an investment bank.
    </p>
    <p><b><u>2 – Entity Type Assessment</u></b><br>
    Most appropriate for: C-Corporations (preferred structure for institutional equity); Holding companies; Pre-IPO entities; Public companies conducting secondary offerings. Corporate governance must meet institutional investor standards.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</u></b><br>
    Before launching an equity sale, companies generally need: Audited or reviewed financial statements; Detailed investor presentation; Defined growth strategy; Legal due diligence preparation; Clean capitalization table. Investment banks conduct internal underwriting and risk evaluation.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</u></b><br>
    Investment banks operate under securities regulations enforced by the U.S. Securities and Exchange Commission and industry oversight by Financial Industry Regulatory Authority (FINRA). Equity sales may be conducted through: Private placements (Reg D); Regulation A offerings; Public offerings (IPO or follow-on); Cross-border institutional placements.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</u></b><br>
    Typical raise sizes include: $5 million to $250+ million, depending on company size; Larger raises for public companies or IPOs. Investment banks generally focus on larger capital raises due to fee economics.
    </p>
    <p><b><u>6 – Capital Round Assessment</u></b><br>
    Equity sale structures may include: Common stock issuance; Preferred stock issuance; Convertible preferred equity; Secondary share sales (existing shareholders selling stock). The structure depends on investor demand and strategic goals.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</u></b><br>
    Capital may be raised: In a single closing; Through multiple closings; In stages tied to valuation milestones; As a public offering with immediate settlement. Institutional deals often close upon full subscription.
    </p>
    <p><b><u>8 – Use of Funds Assessment</u></b><br>
    Typical uses include: Geographic expansion; Product development; Acquisitions; Debt reduction; Working capital. Full disclosure of use of proceeds is mandatory.
    </p>
    <p><b><u>9 – Risk Assessment</u></b><br>
    Risk level: Moderate to High. Risks include: Equity dilution; Loss of control; Board restructuring; Investor governance rights; Market volatility affecting valuation. Public offerings introduce ongoing reporting obligations.
    </p>
    <p><b><u>10 – Capital Cost Assessment</u></b><br>
    Costs typically include: Investment bank underwriting or placement fees (often 4%–8%); Legal and accounting expenses; Roadshow and marketing expenses; Potential warrant coverage. Equity sale results in permanent ownership dilution.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</u></b><br>
    Upfront expenses are high, including: Financial audits; Legal documentation; Prospectus or offering memorandum; Regulatory filings; Due diligence preparation. Preparation costs can reach significant levels before capital is secured.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</u></b><br>
    Typical timeline: 4–9 months, depending on: Financial readiness; Regulatory process; Investor appetite; Market conditions. IPO processes may extend beyond 9 months.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
