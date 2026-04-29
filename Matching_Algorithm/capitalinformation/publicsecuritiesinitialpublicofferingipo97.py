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

def publicsecuritiesinitialpublicofferingipo(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Public Securities</b></u><br>
    Capital Type: Initial Public Offering (IPO) </center></p>
    <p><b><u>Introduction</u></b><br>
    An Initial Public Offering (IPO) is the process through which a privately held company offers its shares to the public for the first time by listing on a stock exchange to raise equity capital. {n} fits that definition. IPOs allow companies to access large-scale public funding, enhance corporate visibility, and provide liquidity to early investors. In the United States, IPO transactions are regulated by the Securities Act of 1933 and supervised by the U.S. Securities and Exchange Commission. Investment banks typically act as underwriters to structure, price, and distribute IPO shares in public markets.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    1. An IPO is a primary market transaction in which a company issues new shares to the public to raise expansion capital. The process involves financial auditing, regulatory disclosure, valuation assessment, and underwriting arrangements. IPOs may be conducted through fixed-price offerings or book-building mechanisms depending on market structure and regulatory approval. After listing, the company's shares are traded freely on public exchanges such as NASDAQ or New York Stock Exchange.<br><br>
    2. IPO financing is best suited for mature, high-growth companies with strong revenue performance, predictable cash flows, and established market presence. Technology firms, manufacturing companies, and large-scale service enterprises frequently pursue IPOs to finance expansion, research development, and debt reduction. Companies generally require institutional investor interest and strong corporate governance structures before going public.<br><br>
    3. IPO issuance is strictly regulated under federal securities law to ensure investor protection and market transparency. Companies must file a registration statement such as Form S-1 with the U.S. Securities and Exchange Commission. Disclosure requirements include financial statements, risk factors, management compensation, and business strategy. The underwriting process may involve syndicates of investment banks that assume distribution risk.<br><br>
    4. IPO transactions are expensive due to underwriting fees, legal compliance costs, and disclosure requirements. Market volatility may cause share price fluctuations after listing. Founders and early investors may experience ownership dilution and potential loss of control. Additionally, public companies face continuous reporting obligations and investor scrutiny.<br><br>
    5. To conduct an IPO, companies must demonstrate sustained financial performance, strong corporate governance, audited financial records, and scalable business operations. Regulatory approval, investor roadshows, and underwriting agreements are essential components of the process. Successful IPOs depend on favorable market conditions, competitive valuation, and credible growth prospects.
    </p>
    <p><u><b>References</u></b><br>
    1. U.S. Securities and Exchange Commission. (2023). Going Public: An Overview. https://www.sec.gov/education/smallbusiness/goingpublic<br>
    2. NASDAQ. (n.d.). IPO Listing Requirements. https://www.nasdaq.com/market-activity/ipos<br>
    3. Securities Act of 1933. https://www.sec.gov/about/laws/sa33.pdf<br>
    4. Investopedia. (n.d.). Initial Public Offering (IPO) Definition. https://www.investopedia.com/terms/i/ipo.asp<br>
    5. Harvard Business Review. (2020). The IPO Decision. https://hbr.org
    </p>
    <p><b><u>Legal Qualification Requirements</b></u><br>
    • Compliance with the Securities Act of 1933<br>
    • SEC Registration Filing (Form S-1)<br>
    • Financial Statement Audit Requirements<br>
    • Underwriting Agreement Execution<br>
    • Corporate Governance Compliance<br>
    • AML/KYC Verification<br>
    • Exchange Listing Approval<br>
    • Disclosure of Material Risks
    </p>
    <p><b><u>Supporting Document List</b></u><br>
    • IPO Prospectus<br>
    • Form S-1 Registration Statement<br>
    • Underwriting Agreement<br>
    • Audited Financial Statements (3–5 years typically)<br>
    • Capitalization Table<br>
    • Roadshow Investor Presentation<br>
    • Corporate Bylaws and Governance Documents<br>
    • Legal Opinion Letters<br>
    • Risk Disclosure Documents
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def publicsecuritiesinitialpublicofferingipofaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Public Securities<br>
    Initial Public Offering (IPO)</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is an Initial Public Offering (IPO)?</u></b><br>
    • Answer: An Initial Public Offering (IPO) is the process by which a private company offers its shares to the public for the first time by listing on a public stock exchange.
    </p>
    <p><u><b>2. Why do companies go public through an IPO?</u></b><br>
    • Answer: Companies conduct IPOs to raise expansion capital, improve liquidity, increase brand credibility, and provide exit opportunities for early investors.
    </p>
    <p><u><b>3. Which stock exchanges are commonly used for IPO listings?</u></b><br>
    • Answer: Common IPO listings occur on exchanges such as New York Stock Exchange and NASDAQ.
    </p>
    <p><u><b>4. Who regulates IPO offerings?</u></b><br>
    • Answer: IPOs are regulated by authorities such as the U.S. Securities and Exchange Commission to ensure disclosure and investor protection.
    </p>
    <p><u><b>5. How are IPO share prices determined?</u></b><br>
    • Answer: IPO pricing is determined through valuation analysis, investor demand, underwriting negotiations, and market conditions.
    </p>
    <p><u><b>6. What is an underwriter in an IPO?</u></b><br>
    • Answer: An underwriter is typically an investment bank that helps structure, price, and distribute shares to institutional and retail investors.
    </p>
    <p><u><b>7. What documents are required for an IPO?</u></b><br>
    • Answer: Required documents include a prospectus, audited financial statements, regulatory filings, and corporate governance disclosures.
    </p>
    <p><u><b>8. Does an IPO cause ownership dilution?</u></b><br>
    • Answer: Yes, issuing new shares during an IPO dilutes existing shareholders' ownership percentage.
    </p>
    <p><u><b>9. What are the advantages of going public?</u></b><br>
    • Answer: Advantages include access to large capital pools, enhanced market visibility, and improved company valuation.
    </p>
    <p><u><b>10. What are the risks of an IPO?</u></b><br>
    • Answer: Risks include regulatory compliance costs, market price volatility, disclosure obligations, and potential loss of control.
    </p>
    <p><u><b>11. How long does the IPO process take?</u></b><br>
    • Answer: The IPO process may take several months, depending on financial preparation, regulatory review, and market conditions.
    </p>
    <p><u><b>12. What is a lock-up period in IPOs?</u></b><br>
    • Answer: A lock-up period is a restriction preventing insiders from selling shares for a specified time after the IPO.
    </p>
    <p><u><b>13. Who can invest in an IPO?</u></b><br>
    • Answer: IPOs are generally open to institutional investors and retail investors subject to exchange and regulatory rules.
    </p>
    <p><u><b>14. What is the difference between IPO and private equity financing?</u></b><br>
    • Answer: IPOs raise capital from public markets, while private equity financing involves private investors purchasing company ownership stakes.
    </p>
    <p><u><b>15. When should a company consider an IPO?</u></b><br>
    • Answer: A company should consider an IPO when it has stable financial performance, strong growth prospects, and the ability to meet public reporting requirements.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def publicsecuritiesinitialpublicofferingipotwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Public Securities</b></u><br>
    Capital Type: Initial Public Offering (IPO)</p></center>
    <p><b><u>1 – Stage of Development Assessment</b></u><br>
    An IPO is best suited for mature growth-stage or large operating companies with strong revenue history, audited financial statements, established governance and compliance systems, and high market scalability potential. Companies are typically beyond early venture stages before pursuing an IPO. {stage} is {{stage}} typical for IPO candidates.
    </p>
    <p><b><u>2 – Entity Type Assessment</b></u><br>
    The preferred structure is a C-Corporation. Public listing is usually conducted on major exchanges such as New York Stock Exchange and Nasdaq. Companies must meet exchange listing standards and corporate governance requirements. {{entity}} is {{entity}} appropriate for IPO listing.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</b></u><br>
    Before IPO launch, companies generally require multiple years of financial reporting, audited financial statements, investment bank underwriting preparation, SEC registration filing readiness, and internal compliance and board approval. The process is highly regulated by the U.S. Securities and Exchange Commission. {{preraise}} reflects {{preraise}} typical IPO readiness.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</b></u><br>
    IPO securities are issued in the public capital market through a registered public offering process. Key participants include underwriters, institutional investors, retail investors, and investment banks. {{premarket}} reflects {{premarket}} market positioning.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</b></u><br>
    IPO capital raises typically range from $100 million to several billion dollars. The size depends on company valuation, market demand, and underwriting strategy. {{raisegoal}} aligns with IPO typical raise sizes.
    </p>
    <p><b><u>6 – Capital Round Assessment</b></u><br>
    IPO represents a primary public equity issuance. Securities offered may include common shares, preferred conversion shares (if structured), and employee stock option pool expansions. This results in permanent equity dilution. {{tranch}} represents {{tranch}} structure.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</b></u><br>
    IPO capital is usually raised through a single public offering closing with possible greenshoe or over-allotment option exercised by underwriters. Shares are allocated during the book-building and roadshow process. {{rounds}} reflects {{rounds}} structure.
    </p>
    <p><b><u>8 – Use of Funds Assessment</b></u><br>
    Common uses of IPO proceeds include expansion and scaling operations, debt repayment, research and development, acquisitions, and working capital strengthening. Full disclosure of fund utilization is required. {{useoffund}} represents {{useoffund}} typical uses.
    </p>
    <p><b><u>9 – Risk Assessment</b></u><br>
    Risk level: Moderate to High. Risks include market volatility after listing, regulatory reporting burden, shareholder activism, and price fluctuation during lock-up expiration. Post-IPO performance depends on market perception and business execution.
    </p>
    <p><b><u>10 – Capital Cost Assessment</b></u><br>
    Capital cost is primarily equity dilution plus underwriting fees (typically 5%–7%), legal and audit costs, and marketing and roadshow expenses. Ownership is permanently diluted after issuance. {{enterprisecost}} reflects {{enterprisecost}} cost profile.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</b></u><br>
    Upfront costs are very high, often $1 million to $5 million+, including SEC registration and filing fees, investment bank underwriting fees, legal and accounting preparation, and exchange listing costs. {{upfrontcost}} reflects {{upfrontcost}} typical IPO costs.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</b></u><br>
    The IPO process is slow, typically 9–18 months, including financial preparation, regulatory filing, underwriter selection, roadshow marketing, pricing and listing execution. {{upfronttime}} reflects {{upfronttime}} expected IPO timeline.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
