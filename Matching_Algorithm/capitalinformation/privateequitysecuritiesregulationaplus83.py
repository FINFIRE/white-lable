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

def privateequitysecuritiesregulationaplus(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = """
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Regulation A Plus</center></p>
    <p><b><u>Introduction</u></b><br>
    Regulation A+ (Reg A+) is a type of securities offering that allows early-stage and growth companies to raise capital from the public with simplified disclosure requirements compared to a traditional IPO. {n} fits that definition. Reg A+ has become a popular method for U.S. companies seeking to access public investors while minimizing regulatory burden. For example, in 2022, over 200 companies utilized Reg A+ offerings to raise more than $500 million collectively. Companies leveraging Reg A+ can accept investments from both accredited and non-accredited investors, expanding the potential capital base. Average fundraising amounts typically range from $1 million to $75 million depending on Tier 1 or Tier 2 offerings. While Reg A+ provides a streamlined path to public funding, it involves regulatory compliance, ongoing reporting obligations, and potential market scrutiny, which may affect suitability for some companies.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1. Regulation A+ is a public offering framework under the U.S. Securities and Exchange Commission (SEC) that enables companies to raise capital from the public without undergoing a full IPO. It consists of two tiers: Tier 1 allows up to $20 million in a 12-month period, and Tier 2 allows up to $75 million. Companies must file an offering circular with the SEC but enjoy reduced disclosure and reporting compared to traditional IPOs. This mechanism provides an opportunity for companies to raise funds from a broader investor base while maintaining compliance with federal securities laws (SEC, n.d.).<br>
    <br>2. The ideal companies for a Reg A+ offering are early-stage or growth-stage firms seeking to raise capital from a wide public investor base, including both accredited and non-accredited investors. Businesses with a clear growth strategy, scalable operations, and a compelling market opportunity benefit most. Companies in sectors like technology, consumer products, and renewable energy often leverage Reg A+ to fund product development, expansion, or marketing initiatives while avoiding the high costs and complexity of a full IPO (WPAB, 2025).<br>
    <br>3. Regulation A was originally introduced in 1933 as a "mini-public offering" exemption but was significantly updated under the JOBS Act of 2012 to create Regulation A+. The revision aimed to increase access to capital for small and medium-sized enterprises by reducing regulatory hurdles while still protecting investors. Since its adoption, Reg A+ has become a viable alternative to traditional private placements and crowdfunding, providing U.S. companies with a flexible route to raise public capital while fostering investor participation (ArtesianVC, 2021).<br>
    <br>4. Despite its advantages, Reg A+ offerings carry several risks. Compliance with SEC disclosure requirements, although reduced compared to a full IPO, still involves legal, accounting, and administrative costs. Public reporting obligations under Tier 2, including annual, semiannual, and current event reports, can be burdensome. Additionally, market risk and investor expectations can affect stock liquidity and valuation. Companies must also manage investor communications carefully to avoid regulatory issues. Political or economic shifts affecting securities regulations can further impact offering success (The CEO Strategy, 2024).<br>
    <br>5. To raise capital via Reg A+, companies must file an offering statement (Form 1-A) with the SEC, including a detailed offering circular, financial statements, and business descriptions. Tier 2 offerings require audited financials and ongoing reporting. Companies must also demonstrate operational readiness, proper corporate governance, and compliance with state "blue sky" laws. A compelling offering circular that clearly communicates business strategy, growth potential, and investment risks is crucial for attracting investors. Companies should engage legal and financial advisors to navigate the SEC filing and disclosure process (SEC, n.d.).
    </p>
    <p><u><b>References</u></b><br>
    U.S. Securities and Exchange Commission (SEC). (n.d.). Regulation A Offerings. https://www.sec.gov/smallbusiness/exemptofferings/regulationa<br>
    FasterCapital. (n.d.). Government funding: How to access public funds and programs for your startup. https://fastercapital.com/content/Government-funding--How-to-access-public-funds-and-programs-for-your-startup.html<br>
    WPAB. (2025). 7 Best Social Impact Accelerators for NGOs Seeking Business Funding. https://www2.fundsforngos.org/articles/7-best-social-impact-accelerators-for-ngos-seeking-business-funding/<br>
    ArtesianVC. (2021). Timeline History: The Evolution of Startup Incubators & Accelerators. https://www.artesianinvest.com/post/timeline-history-the-evolution-of-startup-incubators-accelerators<br>
    The CEO Strategy. (2024). Are public offerings via Reg A+ worth it? (Pros & Cons). https://theceostrategy.com/blogs/business-strategy/are-startup-accelerators-worth-it-pros-cons
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Legally Registered – Must be a corporation or LLC in good standing<br>
    · SEC Filing – Submission of Form 1-A and offering circular required<br>
    · Tier Compliance – Must adhere to Tier 1 or Tier 2 limits<br>
    · Audited Financials – Required for Tier 2 offerings<br>
    · Governance – Appropriate board structure and corporate policies<br>
    · Reporting Obligations – Annual, semiannual, and current reporting for Tier 2<br>
    · Investor Compliance – Ensure investor eligibility and disclosure compliance
    </p>
    <p><b><u>Supporting Document List</u></b><br>
    · Form 1-A Filing / Offering Circular<br>
    · Business Plan & Investment Summary<br>
    · Audited Financial Statements (Tier 2)<br>
    · Corporate Governance Documents<br>
    · Board Resolutions Approving the Offering<br>
    · Risk Disclosure Statements<br>
    · Investor Subscription Agreements<br>
    · Marketing Materials / Offering Documents<br>
    · State Blue Sky Filings<br>
    · Compliance Certificates
    </p>
    """
    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationaplusfaq(request):
    introduction = """
    <p><b><center>Capital Market: Private Equity Securities<br>
    Regulation A Plus</center></b></p>
    <p><center><u><b>Frequently Asked Questions</u></b></center></p>
    <p><u><b>1. What is Regulation A+?</u></b><br>
        •Answer: Regulation A+ is an updated version of Regulation A that allows companies to raise larger amounts of capital from both accredited and non-accredited investors with a simplified SEC filing process.
    </p>
    <p><u><b>2. How does Regulation A+ differ from Regulation A?</u></b><br>
        •Answer: Regulation A+ increases the fundraising limits and provides two tiers, offering more flexibility and broader access to public investors compared to the original Regulation A.
    </p>
    <p><u><b>3. What are the tiers under Regulation A+?</u></b><br>
        •Answer: Tier 1 allows companies to raise up to $20 million in a 12-month period, and Tier 2 allows raising up to $75 million, with different reporting and state compliance requirements.
    </p>
    <p><u><b>4. Who can invest in Regulation A+ offerings?</u></b><br>
        •Answer: Both accredited and non-accredited investors can participate, though Tier 2 imposes investment limits on non-accredited investors to protect smaller investors.
    </p>
    <p><u><b>5. Is SEC qualification required for Regulation A+ offerings?</u></b><br>
        •Answer: Yes, offerings must be qualified by the SEC before securities can be sold, ensuring investor protection and legal compliance.
    </p>
    <p><u><b>6. Are financial statements required for Regulation A+ offerings?</u></b><br>
        •Answer: Yes, Tier 1 offerings require reviewed financial statements, while Tier 2 offerings require audited financial statements.
    </p>
    <p><u><b>7. Can companies publicly market Regulation A+ offerings?</u></b><br>
        •Answer: Yes, companies are permitted to advertise and solicit investors publicly after the SEC qualifies their offering.
    </p>
    <p><u><b>8. What types of companies typically use Regulation A+?</u></b><br>
        •Answer: Early-stage, growth-stage, and small to medium enterprises seeking public capital without the cost and complexity of a full IPO often use Regulation A+.
    </p>
    <p><u><b>9. What are the ongoing reporting requirements under Regulation A+?</u></b><br>
        •Answer: Tier 2 issuers must file annual, semi-annual, and current event reports with the SEC, while Tier 1 issuers have limited ongoing reporting obligations.
    </p>
    <p><u><b>10. What are the benefits of Regulation A+?</u></b><br>
        •Answer: Benefits include access to a wide pool of investors, lower compliance costs than a full IPO, marketing flexibility, and the ability to raise significant capital quickly.
    </p>
    <p><u><b>11. What are the risks or disadvantages of Regulation A+?</u></b><br>
        •Answer: Risks include disclosure obligations, regulatory review, investor scrutiny, costs of compliance, and potential dilution for existing shareholders.
    </p>
    <p><u><b>12. Does Regulation A+ cause equity dilution?</u></b><br>
        •Answer: Yes, issuing new securities under Regulation A+ results in ownership dilution for existing shareholders.
    </p>
    <p><u><b>13. Can Regulation A+ securities be publicly traded?</u></b><br>
        •Answer: Yes, Regulation A+ securities can be listed on exchanges or traded over-the-counter if listing requirements are met.
    </p>
    <p><u><b>14. How quickly can a Regulation A+ offering be completed?</u></b><br>
        •Answer: The process can take a few months, depending on SEC review times, company preparation, and the offering tier.
    </p>
    <p><u><b>15. When should a company consider using Regulation A+?</u></b><br>
        •Answer: A company should consider Regulation A+ when it wants to raise substantial capital from both accredited and retail investors with a faster, less costly process than a traditional IPO.
    </p>
    """
    introduction = mark_safe(introduction)
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationaplustwelve(request):
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
    Capital Type: Regulation A Plus</p></center>
    <p><b><u>1 – Stage of Development Assessment</u></b><br>
    Regulation A+ is best suited for growth-stage to mature companies that have a proven operating history, revenue, and a structured business model. Early-stage startups without financial and operational maturity often find Reg A+ too complex and costly. Stage: {stage}
    </p>
    <p><b><u>2 – Entity Type Assessment</u></b><br>
    C-Corporations are the ideal entity type for Reg A+ offerings. LLCs may participate in limited situations, but corporate structures simplify shareholder management, compliance, and reporting requirements. Sole proprietorships are not eligible. Entity: {entity}
    </p>
    <p><b><u>3 – Pre-Capital Assessment</u></b><br>
    Companies should have audited or reviewed financial statements, a clean capitalization table, and operational traction. Prior funding rounds are acceptable, but clarity on equity ownership and prior investor rights is required. Prior Raise: {preraise}
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</u></b><br>
    Reg A+ operates in the public-facing private securities market, allowing companies to raise capital from both accredited and non-accredited investors. The offering requires SEC qualification and state-level compliance. Previous Market: {premarket}
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</u></b><br>
    Reg A+ allows companies to raise up to $75 million in a 12-month period under Tier 2 offerings. Tier 1 allows up to $20 million. This makes it suitable for companies with large-scale capital needs. Raise Goal: {raisegoal}
    </p>
    <p><b><u>6 – Capital Round Assessment</u></b><br>
    Reg A+ functions as a formal equity round, often used as an alternative to a traditional IPO or large late-stage private equity raise. It can also serve as a pre-IPO fundraising vehicle. Round Stage: {tranch}
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</u></b><br>
    Capital is typically raised through rolling closings, where investors subscribe over the offering period until the maximum raise is achieved. This allows staged entry for investors. Rounds: {rounds}
    </p>
    <p><b><u>8 – Use of Funds Assessment</u></b><br>
    Use of funds must be clearly disclosed in the offering circular and may include:
    · Business expansion and scaling
    · Marketing and sales growth
    · Product development
    · Working capital and operational needs
    Use of Funds: {useoffund}
    </p>
    <p><b><u>9 – Risk Assessment</u></b><br>
    Risk is high, including:
    · Regulatory compliance risk
    · Market and shareholder management risk
    · Ongoing reporting and disclosure obligations
    · Reputational risk with a broader investor base
    </p>
    <p><b><u>10 – Capital Cost Assessment</u></b><br>
    Cost of capital includes equity dilution, legal and accounting compliance costs, ongoing reporting expenses, and governance complexity. There is no debt repayment, but shareholder rights may limit flexibility. Enterprise Cost: {enterprisecost}
    </p>
    <p><b><u>11 – Up Front Cost Assessment</u></b><br>
    Upfront costs are very high, often ranging from $500,000 to several million dollars, covering:
    · SEC filing and qualification
    · Legal and accounting fees
    · Audited financial statements
    · Marketing and investor relations
    · Transfer agent and platform costs
    Upfront Cost: {upfrontcost}
    </p>
    <p><b><u>12 – Timing to Capital Assessment</u></b><br>
    Timing is slow, generally 6–12 months from preparation to SEC qualification and subscription closings. Tier 1 offerings may be faster, but Tier 2 requires extensive review and compliance. Upfront Time: {upfronttime}
    </p>
    """
    introduction = mark_safe(introduction.format(stage=stage,entity=entity,preraise=preraise,premarket=premarket,raisegoal=raisegoal,tranch=tranch,rounds=rounds,useoffund=useoffund,enterprisecost=enterprisecost,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)