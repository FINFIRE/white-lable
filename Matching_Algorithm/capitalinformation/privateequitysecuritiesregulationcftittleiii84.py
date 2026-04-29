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

def privateequitysecuritiesregulationcftittleiii(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Regulation CF Tittle III </center></p>
    <p><b><u>Introduction</u></b><br>
    Regulation Crowdfunding (Reg CF), established under Title III of the Jumpstart Our Business Startups (JOBS) Act of 2012, allows early-stage and private companies to raise capital from the general public through SEC-registered online crowdfunding platforms. {n} fits that definition. Reg CF was designed to democratize investment opportunities by permitting both accredited and non-accredited investors to participate in startup financing within regulated limits. Since its implementation in 2016, companies have collectively raised billions of dollars under Reg CF, with annual funding volumes steadily increasing. The exemption allows eligible companies to raise up to $5 million within a 12-month period. While Reg CF expands access to capital and investor participation, it also imposes disclosure requirements, funding caps, and compliance obligations that companies must carefully manage.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    1. Regulation Crowdfunding (Reg CF) is a securities exemption adopted by the U.S. Securities and Exchange Commission under Title III of the JOBS Act, enabling private companies to raise funds from a large number of investors through SEC-registered online intermediaries, such as funding portals or broker-dealers. Companies may offer equity, debt securities, convertible notes, or other permitted instruments, subject to annual fundraising caps and disclosure requirements. Reg CF aims to facilitate capital formation for startups while maintaining investor protection through regulated platforms and mandatory filings (SEC, n.d.).<br><br>
    2. Reg CF is best suited for early-stage startups, consumer-facing businesses, social enterprises, and growth companies seeking smaller funding rounds while building community engagement. Companies with strong brand narratives, innovative products, and active customer bases often benefit most from crowdfunding campaigns. Businesses seeking between $100,000 and $5 million, particularly those wanting to convert customers into shareholders, frequently leverage Reg CF as an alternative to angel or venture capital financing (Investopedia, n.d.).<br><br>
    3. Reg CF emerged from the JOBS Act of 2012, enacted to stimulate entrepreneurship and improve access to capital following the 2008 financial crisis. Prior to Title III, securities laws largely restricted private investments to accredited investors. The introduction of Reg CF in 2016 marked a significant shift by opening private investment opportunities to retail investors under controlled limits. Amendments in 2020 increased the annual fundraising cap from $1.07 million to $5 million, expanding its usefulness for growing companies (SEC, 2020).<br><br>
    4. Despite its accessibility, Reg CF carries several risks and constraints. Companies must publicly disclose financial statements, business information, and risk factors, which may expose sensitive details to competitors. Fundraising caps limit the maximum capital that can be raised annually. Administrative costs, platform fees, and compliance requirements may reduce net proceeds. Additionally, companies may face shareholder management challenges due to a large number of small investors, potentially complicating future financing rounds (Harvard Law School Forum, 2022).<br><br>
    5. To conduct a Reg CF offering, companies must file Form C with the SEC, disclose financial information, business operations, and intended use of proceeds, and launch the campaign through an SEC-registered crowdfunding portal. Investor investment limits apply based on income and net worth. Successful campaigns typically require strong marketing strategies, clear communication, compelling storytelling, and transparent risk disclosures. Companies must also file annual reports (Form C-AR) to maintain compliance until reporting obligations are terminated (SEC, n.d.).
    </p>
    <p><u><b>References</u></b><br>
    1. U.S. Securities and Exchange Commission. (n.d.). Regulation Crowdfunding (Reg CF). https://www.sec.gov<br>
    2. Investopedia. (n.d.). Regulation Crowdfunding (Reg CF). https://www.investopedia.com<br>
    3. Harvard Law School Forum on Corporate Governance. (2022). Crowdfunding disclosure and compliance considerations. https://corpgov.law.harvard.edu<br>
    4. U.S. Securities and Exchange Commission (SEC). (2020). Amendments to Regulation Crowdfunding. https://www.sec.gov
    </p>
    <p><b><u>Legal Qualification Requirements</b></u><br>
    • U.S.-based Entity – Must be organized in the United States<br>
    • SEC Filing – Submission of Form C before launch<br>
    • Registered Intermediary – Must use SEC-registered crowdfunding portal or broker<br>
    • Fundraising Cap – Maximum $5 million in a 12-month period<br>
    • Financial Disclosure – Required financial statements (reviewed or audited depending on raise size)<br>
    • Investor Limits – Must comply with individual investment caps<br>
    • Ongoing Reporting – Annual Form C-AR filing required<br>
    • AML/KYC Compliance – Investor identity verification required
    </p>
    <p><b><u>Supporting Document List</b></u><br>
    • Form C Filing<br>
    • Business Plan & Offering Summary<br>
    • Financial Statements (reviewed or audited if required)<br>
    • Risk Disclosure Statement<br>
    • Use of Proceeds Description<br>
    • Cap Table & Ownership Structure<br>
    • Subscription Agreements<br>
    • Platform Agreement with Funding Portal<br>
    • Annual Report (Form C-AR)
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationcftittleiiifaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Equity Securities<br>
    Regulation CF Tittle III</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is Regulation CF (Title III)?</u></b><br>
    • Answer: Regulation Crowdfunding (Reg CF), created under Title III of the JOBS Act, allows private companies to raise capital from the general public through SEC-registered crowdfunding platforms.
    </p>
    <p><u><b>2. How much capital can be raised under Regulation CF?</u></b><br>
    • Answer: Companies can raise up to $5 million within a 12-month period under Regulation CF.
    </p>
    <p><u><b>3. Who can invest in a Regulation CF offering?</u></b><br>
    • Answer: Both accredited and non-accredited investors can participate, subject to annual investment limits based on income and net worth.
    </p>
    <p><u><b>4. Where must Regulation CF offerings be conducted?</u></b><br>
    • Answer: Offerings must be conducted through SEC-registered intermediary platforms, either broker-dealers or funding portals.
    </p>
    <p><u><b>5. Is SEC filing required for Regulation CF?</u></b><br>
    • Answer: Yes, companies must file Form C with the SEC, providing required disclosures before launching the offering.
    </p>
    <p><u><b>6. Are financial statements required under Regulation CF?</u></b><br>
    • Answer: Yes, financial statement requirements vary depending on the amount raised and may require review or audit by a CPA.
    </p>
    <p><u><b>7. Can companies advertise Regulation CF offerings?</u></b><br>
    • Answer: Companies may engage in limited advertising but must direct investors to the official crowdfunding platform for full details.
    </p>
    <p><u><b>8. What types of securities can be offered under Regulation CF?</u></b><br>
    • Answer: Companies may offer equity, convertible notes, SAFEs, or debt securities through Regulation CF.
    </p>
    <p><u><b>9. Are there ongoing reporting requirements?</u></b><br>
    • Answer: Yes, companies must file annual reports with the SEC until certain termination conditions are met.
    </p>
    <p><u><b>10. Does Regulation CF cause ownership dilution?</u></b><br>
    • Answer: Yes, issuing equity or convertible securities under Regulation CF results in dilution of existing shareholders.
    </p>
    <p><u><b>11. What are the benefits of Regulation CF?</u></b><br>
    • Answer: Benefits include access to retail investors, marketing exposure, community engagement, and relatively lower fundraising thresholds.
    </p>
    <p><u><b>12. What are the risks of using Regulation CF?</u></b><br>
    • Answer: Risks include public disclosure requirements, administrative complexity, shareholder management challenges, and compliance costs.
    </p>
    <p><u><b>13. How long does a Regulation CF offering typically last?</u></b><br>
    • Answer: Offerings typically remain open for several weeks to a few months, depending on fundraising goals and platform timelines.
    </p>
    <p><u><b>14. Can a company use Regulation CF alongside other exemptions?</u></b><br>
    • Answer: Yes, companies can combine Regulation CF with other exemptions such as Regulation D or Regulation A, subject to compliance rules.
    </p>
    <p><u><b>15. When should a company consider Regulation CF?</u></b><br>
    • Answer: A company should consider Regulation CF when it seeks to raise early-stage capital from a broad base of public investors while building brand visibility and community support.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationcftittleiiitwelve(request):
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
    Capital Type: Regulation CF Tittle III</p></center>
    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    Regulation CF (Title III) is best suited for early-stage to growth-stage companies, including startups that have launched a product or demonstrated early traction. It is commonly used by companies that are not yet ready for institutional venture capital. {stage} aligns with this profile.
    </p>
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    C-Corporations are the most common structure for Reg CF offerings due to shareholder management efficiency. LLCs may qualify, but complexity increases with larger investor pools. Sole proprietorships are not eligible. {{n}}'s entity type of {{entity}} is {{entity}} suitable for Regulation CF offerings.
    </p>
    <p><b><u>3 - Pre-Capital Assessment</b></u><br>
    Companies may have minimal prior funding. Founder capital and small angel rounds are acceptable, but capitalization tables must be organized. Financial disclosures are required, and reviewed or audited financial statements may be necessary depending on the raise amount. {{n}}'s pre-raise capital status of {{preraise}} demonstrates {{preraise}} prior fundraising activity.
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    Reg CF operates in the regulated crowdfunding securities market, allowing companies to raise funds from both accredited and non-accredited investors through SEC-registered crowdfunding portals. {{n}}'s pre-market positioning of {{premarket}} reflects {{premarket}} market presence prior to the offering.
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    Companies may raise up to $5 million within a 12-month period under Regulation CF, making it suitable for small to mid-sized capital raises. {{n}}'s target raise goal of {{raisegoal}} aligns with Regulation CF fundraising parameters.
    </p>
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Reg CF functions as a formal equity round, typically used at the seed or early growth stage. Securities offered may include common equity, preferred equity, SAFEs, or convertible instruments. {{n}}'s {{tranch}} tranching structure is {{tranch}} representative of Regulation CF capital rounds.
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Capital is raised through rolling subscriptions during the live campaign period, with funds typically released upon reaching the minimum funding target. {{n}}'s planned {{rounds}} rounds configuration reflects {{rounds}} tranche scheduling approach for capital deployment.
    </p>
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Use of funds must be clearly disclosed in the offering documents and commonly includes product development, marketing and customer acquisition, hiring and operational scaling, and working capital. {{n}}'s intended use of funds for {{useoffund}} aligns with typical Reg CF deployment patterns.
    </p>
    <p><b><u>9 - Risk Assessment</b></u><br>
    Risk is high, including public disclosure risk, reputational exposure, administrative burden of managing many small investors, and execution risk if funding targets are not met. Investors also face high illiquidity and startup failure risk.
    </p>
    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    Cost of capital includes equity dilution, portal fees (typically 5–10%), legal and compliance costs, and ongoing investor communication obligations. {{n}}'s enterprise cost profile of {{enterprisecost}} reflects {{enterprisecost}} capital cost considerations.
    </p>
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    Upfront costs are moderate, including legal preparation, financial statement review or audit, marketing expenses, and portal setup fees. {{n}}'s upfront cost estimate of {{upfrontcost}} is {{upfrontcost}} typical for Regulation CF offerings.
    </p>
    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    Timing is moderate, generally 3–6 months, including preparation, SEC filing (Form C), campaign launch, and funding period completion. {{n}}'s anticipated time to capital of {{upfronttime}} reflects {{upfronttime}} timeline expectations for Regulation CF fundraising processes.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)