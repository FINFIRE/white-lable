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

def privateequitysecuritiesregulationa(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = """
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Regulation A</center></p>
    <p><b><u>Introduction</u></b><br>
    Regulation A is a securities exemption that allows companies to raise capital from the public without completing a full traditional IPO registration process. {n} fits that definition. Regulation A has become increasingly popular as an alternative path to public capital markets, allowing companies to access both accredited and non-accredited investors. The framework was significantly updated under the JOBS Act of 2012 to create Regulation A+, which expanded fundraising limits and reduced compliance burden. Companies utilizing Regulation A can raise up to $75 million within a 12-month period under Tier 2 offerings, making it a viable alternative to traditional IPOs for growth-stage companies. While Regulation A provides streamlined access to public capital, it still requires SEC qualification, ongoing reporting obligations, and careful investor relations management.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1. Regulation A is a securities exemption framework under the U.S. Securities and Exchange Commission (SEC) that enables companies to raise capital from the public with simplified disclosure requirements compared to a traditional IPO. The framework consists of Tier 1 and Tier 2, offering flexibility based on capital raising needs and company maturity. Companies must file an offering statement with the SEC but enjoy reduced disclosure and reporting obligations compared to full IPOs. (SEC, n.d.)<br>
    <br>2. The ideal companies for a Regulation A offering are growth-stage firms seeking to raise capital from both accredited and non-accredited investors without the complexity of a full IPO. Businesses with proven operations, clear growth strategies, and scalable models benefit most from Regulation A. Companies in technology, consumer products, renewable energy, and emerging sectors often leverage Regulation A to fund expansion and market growth. (ArtesianVC, 2021)<br>
    <br>3. Regulation A was originally introduced in 1933 as a "mini-public offering" exemption but was significantly modernized under the JOBS Act of 2012 to create Regulation A+. This update aimed to increase capital access for small and medium-sized enterprises by reducing regulatory hurdles while protecting investors. Since adoption, Reg A has become a practical alternative to traditional private placements and crowdfunding. (The CEO Strategy, 2024)<br>
    <br>4. Despite its advantages, Regulation A offerings carry regulatory, operational, and market risks. SEC compliance, although simplified, still involves substantial legal and accounting costs. Tier 2 offerings require ongoing annual and semiannual reporting, which can be burdensome. Public reporting obligations create reputational exposure, and investor expectations may affect stock liquidity and valuation. Additionally, political or economic changes affecting securities regulations can impact offering success. (WPAB, 2025)<br>
    <br>5. To raise capital via Regulation A, companies must file an offering statement (Form 1-A) with the SEC, including a detailed offering circular, financial statements, and business descriptions. Companies must demonstrate operational readiness, proper governance, and compliance with state blue sky laws. A compelling offering circular that clearly communicates business strategy, growth potential, and investment risks is critical for attracting investors. Companies should engage legal and financial advisors to navigate SEC filing requirements. (SEC, n.d.)
    </p>
    <p><u><b>References</u></b><br>
    U.S. Securities and Exchange Commission (SEC). (n.d.). Regulation A Offerings. https://www.sec.gov/smallbusiness/exemptofferings/regulationa<br>
    ArtesianVC. (2021). Timeline History: The Evolution of Startup Incubators & Accelerators. https://www.artesianinvest.com/post/timeline-history-the-evolution-of-startup-incubators-accelerators<br>
    The CEO Strategy. (2024). Are state grants worth it? (Pros & Cons). https://theceostrategy.com/blogs/business-strategy/are-startup-accelerators-worth-it-pros-cons<br>
    WPAB. (2025). 7 Best Social Impact Accelerators for NGOs Seeking Business Funding. https://www2.fundsforngos.org/articles/7-best-social-impact-accelerators-for-ngos-seeking-business-funding/<br>
    FasterCapital. (n.d.). Government funding: How to access public funds and programs for your startup. https://fastercapital.com/content/Government-funding--How-to-access-public-funds-and-programs-for-your-startup.html
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Legally Registered – Must be a corporation or LLC in good standing<br>
    · SEC Filing – Submission of Form 1-A and offering circular required<br>
    · Tier Compliance – Must adhere to Tier 1 or Tier 2 limits<br>
    · Audited Financials – Required for Tier 2 offerings<br>
    · Governance – Appropriate board structure and corporate policies<br>
    · Reporting Obligations – Annual and current reporting for Tier 2<br>
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
    · Marketing Materials / Offering Documents
    </p>
    """
    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationafaq(request):
    introduction = """
    <p><b><center>Capital Market: Private Equity Securities<br>
    Regulation A</center></b></p>
    <p><center><u><b>Frequently Asked Questions</u></b></center></p>
    <p><u><b>1. What is Regulation A?</u></b><br>
        •Answer: Regulation A is a securities exemption that allows companies to raise capital from the public without completing a full traditional IPO registration process.
    </p>
    <p><u><b>2. How does Regulation A differ from a traditional IPO?</u></b><br>
        •Answer: Regulation A involves a simplified registration and disclosure process compared to a full IPO, resulting in lower costs and faster execution.
    </p>
    <p><u><b>3. What are the tiers under Regulation A?</u></b><br>
        •Answer: Regulation A consists of Tier 1 and Tier 2, which differ in fundraising limits, disclosure requirements, and ongoing reporting obligations.
    </p>
    <p><u><b>4. How much capital can be raised under Regulation A?</u></b><br>
        •Answer: Companies can raise up to $20 million under Tier 1 and up to $75 million under Tier 2 within a 12-month period.
    </p>
    <p><u><b>5. Who can invest in a Regulation A offering?</u></b><br>
        •Answer: Both accredited and non-accredited investors can participate, although Tier 2 imposes investment limits on non-accredited investors.
    </p>
    <p><u><b>6. Is SEC qualification required for Regulation A offerings?</u></b><br>
        •Answer: Yes, offerings must be qualified by the U.S. Securities and Exchange Commission (SEC) before securities can be sold.
    </p>
    <p><u><b>7. Are financial statements required under Regulation A?</u></b><br>
        •Answer: Yes, financial disclosures are required, and Tier 2 offerings typically require audited financial statements.
    </p>
    <p><u><b>8. Can companies publicly market a Regulation A offering?</u></b><br>
        •Answer: Yes, companies are allowed to publicly solicit and advertise their Regulation A offerings once properly filed.
    </p>
    <p><u><b>9. What types of companies use Regulation A?</u></b><br>
        •Answer: Early-stage and growth-stage companies seeking public capital access without a full IPO often use Regulation A.
    </p>
    <p><u><b>10. Are ongoing reporting requirements required under Regulation A?</u></b><br>
        •Answer: Tier 2 issuers must file ongoing reports, while Tier 1 issuers have more limited reporting obligations.
    </p>
    <p><u><b>11. What are the advantages of Regulation A?</u></b><br>
        •Answer: Advantages include access to retail investors, lower compliance costs than an IPO, and broader marketing capabilities.
    </p>
    <p><u><b>12. What are the disadvantages of Regulation A?</u></b><br>
        •Answer: Disadvantages include regulatory review, disclosure requirements, costs of compliance, and potential investor scrutiny.
    </p>
    <p><u><b>13. Does Regulation A cause ownership dilution?</u></b><br>
        •Answer: Yes, issuing equity securities under Regulation A results in ownership dilution for existing shareholders.
    </p>
    <p><u><b>14. Can Regulation A securities be publicly traded?</u></b><br>
        •Answer: Yes, Regulation A securities can be listed on exchanges or traded over-the-counter if listing requirements are met.
    </p>
    <p><u><b>15. When should a company consider Regulation A?</u></b><br>
        •Answer: A company should consider Regulation A when it seeks public capital access, marketing flexibility, and growth funding without pursuing a full IPO.
    </p>
    """
    introduction = mark_safe(introduction)
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationatwelve(request):
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
    Capital Type: Regulation A</p></center>
    <p><b><u>1 – Stage of Development Assessment</u></b><br>
    Regulation A offerings are best suited for growth-stage to mature companies with operating history, revenue, and strong compliance readiness. Early-stage startups generally find Reg A too complex and costly. Stage: {stage}
    </p>
    <p><b><u>2 – Entity Type Assessment</u></b><br>
    C-Corporations are the most suitable entity type. LLCs may qualify in limited cases, but corporate structures are preferred due to shareholder management, reporting, and securities requirements. Sole proprietorships are not eligible. Entity: {entity}
    </p>
    <p><b><u>3 – Pre-Capital Assessment</u></b><br>
    Companies should demonstrate financial statements, operating history, and business traction. Prior capital raises are acceptable, but capitalization tables must be clean and well-documented. Prior Raise: {preraise}
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</u></b><br>
    Regulation A operates in the public-facing private securities market, allowing capital to be raised from both accredited and non-accredited investors, subject to regulatory qualification. Previous Market: {premarket}
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</u></b><br>
    Regulation A allows raises of up to $75 million within a 12-month period, making it suitable for large growth capital needs. Raise Goal: {raisegoal}
    </p>
    <p><b><u>6 – Capital Round Assessment</u></b><br>
    Reg A offerings function as formal equity rounds, often used as alternatives to IPOs or late-stage private equity raises. Round Stage: {tranch}
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</u></b><br>
    Capital is typically raised through rolling subscriptions, allowing continuous investment during the offering period until the maximum raise amount is reached. Rounds: {rounds}
    </p>
    <p><b><u>8 – Use of Funds Assessment</u></b><br>
    Use of funds must be clearly disclosed and strictly followed, commonly including:
    · Expansion and scaling
    · Marketing and brand growth
    · Product development
    · Debt repayment (if disclosed)
    Use of Funds: {useoffund}
    </p>
    <p><b><u>9 – Risk Assessment</u></b><br>
    Risk is high, including regulatory scrutiny, ongoing reporting obligations, market risk, and reputational exposure. Investor relations risk is also significant due to a large shareholder base.
    </p>
    <p><b><u>10 – Capital Cost Assessment</u></b><br>
    Cost of capital includes equity dilution, compliance burden, and ongoing reporting expenses. While there is no repayment obligation, governance complexity increases substantially. Enterprise Cost: {enterprisecost}
    </p>
    <p><b><u>11 – Up Front Cost Assessment</u></b><br>
    Upfront costs are very high, including legal, audit, SEC qualification, marketing, platform fees, and transfer agent costs, often ranging from $500,000 to several million dollars. Upfront Cost: {upfrontcost}
    </p>
    <p><b><u>12 – Timing to Capital Assessment</u></b><br>
    Timing to capital is slow, typically 6–12 months, due to preparation, regulatory review, and marketing requirements. Upfront Time: {upfronttime}
    </p>
    """
    introduction = mark_safe(introduction.format(stage=stage,entity=entity,preraise=preraise,premarket=premarket,raisegoal=raisegoal,tranch=tranch,rounds=rounds,useoffund=useoffund,enterprisecost=enterprisecost,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)