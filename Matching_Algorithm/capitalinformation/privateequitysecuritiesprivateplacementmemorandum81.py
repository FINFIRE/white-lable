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

def privateequitysecuritiesprivateplacementmemorandum(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = """
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Private Placement Memorandum</center></p>
    <p><b><u>Introduction</u></b><br>
    Private Placement Memorandums are used by privately held companies to raise capital from accredited or institutional investors without issuing securities to the general public. They are designed to provide transparency, manage investor expectations, and protect issuers from legal liability by fully disclosing material risks and financial information. {n} fits that definition. PPMs are widely used in private equity and alternative investment markets, particularly in venture capital rounds, real estate syndications, hedge funds, and private debt offerings. According to guidance issued by the U.S. Securities and Exchange Commission, private placements conducted under Regulation D allow companies to raise unlimited capital from accredited investors, provided proper disclosures are made. While PPMs offer flexibility and confidentiality, they involve significant legal preparation costs and are subject to strict securities compliance standards (SEC, n.d.).
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1. A Private Placement Memorandum is a formal disclosure document prepared by a private company when offering securities through a private placement. It outlines essential details such as the company's business model, management team, financial statements, investment structure, risk factors, and exit strategies. Although not always legally required, a PPM is considered best practice for complying with securities laws and minimizing issuer liability in private equity transactions. It serves as the primary communication tool between issuers and prospective investors in private offerings (Investopedia, n.d.).<br>
    <br>2. PPM-based financing is best suited for private companies seeking to raise substantial capital from accredited investors, institutional investors, family offices, or high-net-worth individuals. These companies are often operating in private equity, real estate development, venture-backed startups, infrastructure projects, energy, and alternative investments. Businesses with complex capital structures, higher risk profiles, or long investment horizons benefit most from PPMs, as the document allows detailed risk disclosure and customized investment terms. Companies that prioritize regulatory compliance, investor transparency, and professional fundraising standards are most likely to use a PPM effectively (NVCA, 2023).<br>
    <br>3. Private placement memorandums gained prominence as securities markets evolved to distinguish between public offerings and private capital raising. In the United States and similar jurisdictions, regulatory frameworks such as Regulation D were introduced to allow private offerings while maintaining investor protection through disclosure requirements. Over time, PPMs became standard practice in private equity and alternative investment markets, especially as regulatory scrutiny increased. Today, PPMs are a critical component of private capital markets, balancing capital formation flexibility with investor protection and legal accountability (ArtesianVC, 2021).<br>
    <br>4. Despite their advantages, PPM-based offerings carry several risks and limitations. Preparing a PPM is time-consuming and costly, often requiring legal, accounting, and compliance professionals. Errors, omissions, or misleading disclosures can expose issuers to legal liability and regulatory penalties. From an investor perspective, private placements are illiquid, high-risk investments with limited exit options and reduced transparency compared to public markets. Additionally, reliance on exemptions means offerings are restricted to qualified investors, limiting the available capital pool (Harvard Law School Forum, 2022).<br>
    <br>5. To raise capital using a PPM, a company must first determine the appropriate private placement exemption and target investor group. Legal counsel typically prepares the PPM to ensure compliance with securities laws. The company then distributes the PPM to qualified investors and collects subscriptions through formal agreements. Once investments are accepted, funds are deployed according to the disclosed use-of-proceeds plan. Ongoing investor reporting and compliance obligations continue throughout the investment lifecycle. Accurate documentation and adherence to disclosure commitments are essential for maintaining investor trust and regulatory compliance (SEC, n.d.).
    </p>
    <p><u><b>References</u></b><br>
    Investopedia. (n.d.). Private placement memorandum (PPM). https://www.investopedia.com<br>
    U.S. Securities and Exchange Commission (SEC). (n.d.). Private placements and Regulation D. https://www.sec.gov<br>
    National Venture Capital Association (NVCA). (2023). Private equity fundraising practices. https://nvca.org<br>
    ArtesianVC. (2021). Timeline history: The evolution of startup incubators & accelerators. https://www.artesianinvest.com<br>
    Harvard Law School Forum on Corporate Governance. (2022). Disclosure obligations in private offerings. https://corpgov.law.harvard.edu
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Private Company Status – Issuer must be a privately held entity<br>
    · Securities Law Compliance – Offering must comply with private placement regulations<br>
    · Accredited Investor Rules – Investors must meet qualification standards<br>
    · Full Risk Disclosure – All material risks must be disclosed<br>
    · No Misrepresentation – Information must be accurate and complete<br>
    · AML/KYC Compliance – Investor verification and background checks required<br>
    · Corporate Authorization – Board or shareholder approval for issuance
    </p>
    <p><b><u>Supporting Document List</u></b><br>
    · Private Placement Memorandum (PPM)<br>
    · Subscription Agreement<br>
    · Investor Questionnaire<br>
    · Capitalization Table<br>
    · Financial Statements and Projections<br>
    · Corporate Governance Documents<br>
    · Risk Disclosure Statements<br>
    · Legal Opinions (if required)
    </p>
    """
    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesprivateplacementmemorandumfaq(request):
    introduction = """
    <p><b><center>Capital Market: Private Equity Securities<br>
    Private Placement Memorandum</center></b></p>
    <p><center><u><b>Frequently Asked Questions</u></b></center></p>
    <p><u><b>1. What is a Private Placement Memorandum (PPM)?</u></b><br>
        •Answer: A Private Placement Memorandum (PPM) is a legal disclosure document provided to potential investors when offering securities in a private placement.
    </p>
    <p><u><b>2. What is the purpose of a PPM?</u></b><br>
        •Answer: The purpose of a PPM is to disclose material information about the investment opportunity, risks, financials, and terms to help investors make informed decisions.
    </p>
    <p><u><b>3. Who typically uses a PPM?</u></b><br>
        •Answer: Startups, private companies, real estate syndications, and investment funds commonly use a PPM when raising capital privately.
    </p>
    <p><u><b>4. Is a PPM required by law?</u></b><br>
        •Answer: While not always legally required, a PPM is strongly recommended to comply with securities regulations and reduce liability risk.
    </p>
    <p><u><b>5. What information is included in a PPM?</u></b><br>
        •Answer: A PPM typically includes company overview, management team details, financial statements, risk factors, use of proceeds, and subscription terms.
    </p>
    <p><u><b>6. Who can invest in a private placement offering?</u></b><br>
        •Answer: Private placements are often limited to accredited investors or qualified purchasers, depending on jurisdiction and exemption rules.
    </p>
    <p><u><b>7. Does a PPM guarantee returns?</u></b><br>
        •Answer: No, a PPM clearly outlines investment risks and does not guarantee any specific return.
    </p>
    <p><u><b>8. How does a PPM protect the company?</u></b><br>
        •Answer: It provides full disclosure of risks and material facts, helping reduce legal exposure for misrepresentation claims.
    </p>
    <p><u><b>9. How does a PPM protect investors?</u></b><br>
        •Answer: It ensures investors receive detailed information about risks, structure, and financial condition before committing capital.
    </p>
    <p><u><b>10. Is a PPM used in public offerings?</u></b><br>
        •Answer: No, public offerings use a prospectus, while PPMs are used for private offerings.
    </p>
    <p><u><b>11. What is the difference between a PPM and a pitch deck?</u></b><br>
        •Answer: A pitch deck is a marketing presentation, while a PPM is a formal legal disclosure document.
    </p>
    <p><u><b>12. Can multiple investors participate under one PPM?</u></b><br>
        •Answer: Yes, a PPM governs the terms under which multiple investors can subscribe to the offering.
    </p>
    <p><u><b>13. Who prepares a PPM?</u></b><br>
        •Answer: A PPM is typically prepared by securities attorneys with input from company management and financial advisors.
    </p>
    <p><u><b>14. What risks are disclosed in a PPM?</u></b><br>
        •Answer: Risks may include market risks, operational risks, financial risks, regulatory risks, and potential loss of investment.
    </p>
    <p><u><b>15. When should a company use a PPM?</u></b><br>
        •Answer: A company should use a PPM when raising capital through a private securities offering to ensure regulatory compliance and investor transparency.
    </p>
    """
    introduction = mark_safe(introduction)
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesprivateplacementmemorandumtwelve(request):
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
    Capital Type: Private Placement Memorandum</p></center>
    <p><b><u>1 – Stage of Development Assessment</u></b><br>
    A Private Placement Memorandum (PPM) is suitable for growth-stage to mature companies, as well as certain early-stage ventures seeking structured private capital. It is most commonly used when raising larger, formal equity rounds from accredited investors. Stage: {stage}
    </p>
    <p><b><u>2 – Entity Type Assessment</u></b><br>
    PPM offerings are typically structured through C-Corporations or LLCs, and may involve the creation of a special purpose vehicle (SPV) or investment entity. Sole proprietorships are generally not suitable due to securities compliance requirements. Entity: {entity}
    </p>
    <p><b><u>3 – Pre-Capital Assessment</u></b><br>
    Companies should demonstrate operational history, financial statements, and defined use of proceeds. While early-stage companies may use a PPM, investors generally expect clear traction or a well-developed business plan. Prior Raise: {preraise}
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</u></b><br>
    PPMs operate within the private securities market, typically conducted under securities law exemptions (e.g., private offerings to accredited investors). The offering is not publicly traded and is subject to disclosure requirements. Previous Market: {premarket}
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</u></b><br>
    PPM raises commonly range from $1 million to $50+ million, depending on investor network, valuation, and company scale. Raise Goal: {raisegoal}
    </p>
    <p><b><u>6 – Capital Round Assessment</u></b><br>
    PPMs are often used for formal equity rounds, including growth equity, private equity raises, real estate syndications, or fund formation rounds. Round Stage: {tranch}
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</u></b><br>
    Capital may be raised through rolling closings, allowing investors to subscribe over a defined offering period until the target raise amount is reached. Rounds: {rounds}
    </p>
    <p><b><u>8 – Use of Funds Assessment</u></b><br>
    Use of funds must be clearly disclosed in the memorandum, typically including:
    · Expansion and growth initiatives
    · Acquisitions
    · Product development
    · Working capital
    Use of Funds: {useoffund}
    </p>
    <p><b><u>9 – Risk Assessment</u></b><br>
    Risk is high for investors, as private placements are illiquid and speculative. Companies face regulatory and compliance risk if disclosures are incomplete or misleading.
    </p>
    <p><b><u>10 – Capital Cost Assessment</u></b><br>
    The cost of capital includes equity dilution, investor rights, and potential preferred return structures. While there is no repayment obligation, ownership and governance impact can be significant. Enterprise Cost: {enterprisecost}
    </p>
    <p><b><u>11 – Up Front Cost Assessment</u></b><br>
    Upfront costs are high, including legal drafting, securities compliance, offering documentation, filing fees, and potential placement agent fees. Upfront Cost: {upfrontcost}
    </p>
    <p><b><u>12 – Timing to Capital Assessment</u></b><br>
    Timing to capital is moderate to slow, typically 3–6 months or longer, depending on legal preparation, investor outreach, and subscription commitments. Upfront Time: {upfronttime}
    </p>
    """
    introduction = mark_safe(introduction.format(stage=stage,entity=entity,preraise=preraise,premarket=premarket,raisegoal=raisegoal,tranch=tranch,rounds=rounds,useoffund=useoffund,enterprisecost=enterprisecost,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)