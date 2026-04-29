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

def privateequitysecuritiesrule144(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Rule 144 </center></p>
    <p><b><u>Introduction</u></b><br>
    Rule 144 Securities are ideal for investors, founders, and early stakeholders seeking a regulated pathway to liquidity for privately issued or restricted securities. They are designed so that holders of restricted or control securities may resell them publicly or privately once specific holding periods, disclosure, and volume requirements are satisfied under U.S. securities law. {n} fits that definition.
    In 2026, Rule 144 remains a cornerstone of private equity and venture-backed liquidity planning, commonly used by founders, employees, early investors, and affiliates following private placements, Regulation D offerings, or mergers. The rule provides a structured bridge between private capital formation and public market liquidity without requiring a full SEC registration.
    While Rule 144 enables lawful resale, it introduces timing, compliance, and market risk. Failure to meet holding periods, affiliate conditions, or public information requirements can invalidate resale eligibility and expose sellers to regulatory enforcement.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    1. Rule 144 is a safe-harbor provision under the U.S. Securities Act of 1933 that permits the public resale of restricted and control securities if specific conditions relating to holding period, volume, manner of sale, and disclosure are met. (U.S. Securities and Exchange Commission, 2025)<br><br>
    2. Securities sold under Rule 144 remain part of the Private Equity Securities market until resale conditions are satisfied, at which point they may transition into freely tradable public securities. The rule does not exempt the original issuance, only the resale. (SEC, 2025)<br><br>
    3. Legally, Rule 144 applies differently to affiliates and non-affiliates of the issuer. Affiliates face ongoing volume limits and reporting requirements, while non-affiliates may sell freely after meeting the applicable holding period and public information criteria. (Practising Law Institute, 2025)<br><br>
    4. From a risk perspective, Rule 144 exposes sellers to liquidity timing risk, market volatility, and compliance risk. Market conditions at the time of eligibility may materially affect realized value, and improper resale can result in rescission liability. (Harvard Law School Forum, 2025)<br><br>
    5. From an accounting and process standpoint, Rule 144 resales convert restricted securities into unrestricted securities, removing resale limitations once conditions are met. Issuers and transfer agents play a critical role in legend removal and compliance verification. (Deloitte, 2025)
    </p>
    <p><u><b>References</u></b><br>
    U.S. Securities and Exchange Commission (SEC). (2025). Rule 144: Selling Restricted and Control Securities. https://www.sec.gov/reportspubs/investor-publications/investorpubsrule144<br>
    Practising Law Institute (PLI). (2025). Resales of Restricted Securities under Rule 144. https://www.pli.edu<br>
    Harvard Law School Forum on Corporate Governance. (2025). Liquidity Pathways for Private Securities. https://corpgov.law.harvard.edu<br>
    Deloitte. (2025). Accounting and Disclosure for Equity Transactions. https://www2.deloitte.com/equity<br>
    CFA Institute. (2025). Private Market Liquidity and Regulation. https://www.cfainstitute.org
    </p>
    <p><b><u>Legal Qualification Requirements</b></u><br>
    • Restricted or Control Securities – Securities acquired through private placement<br>
    • Holding Period – Minimum 6 or 12 months, depending on issuer status<br>
    • Affiliate Status Assessment – Insider or control person determination<br>
    • Volume Limitations – Sales caps for affiliates<br>
    • Public Information Requirement – Current issuer disclosures<br>
    • Manner of Sale – Brokered or compliant transaction methods<br>
    • Legend Removal Approval – Issuer or transfer agent confirmation<br>
    • Form 144 Filing – Required notice for affiliate sales
    </p>
    <p><b><u>Supporting Document List</b></u><br>
    • Stock Purchase or Subscription Agreement – Original acquisition proof<br>
    • Share Certificates / Book-Entry Records – Ownership documentation<br>
    • Legal Opinion Letter – Rule 144 eligibility confirmation<br>
    • Transfer Agent Instructions – Legend removal authorization<br>
    • Form 144 Filing – SEC resale notice (if applicable)<br>
    • Issuer Public Filings – Disclosure compliance evidence<br>
    • Board or Officer Certifications – Affiliate status confirmation<br>
    • Brokerage Confirmations – Manner-of-sale compliance
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def privateequitysecuritiesrule144faq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Equity Securities – Rule 144<br>
    Private Equity / Restricted Securities</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is SEC Rule 144?</u></b><br>
    • Answer: SEC Rule 144 is a regulation that provides a safe harbor for the public resale of restricted and control securities without full SEC registration.
    </p>
    <p><u><b>2. What are restricted securities under Rule 144?</u></b><br>
    • Answer: Restricted securities are securities acquired in unregistered, private transactions such as private placements or employee equity compensation.
    </p>
    <p><u><b>3. What are control securities under Rule 144?</u></b><br>
    • Answer: Control securities are securities held by affiliates of the issuing company, regardless of how they were acquired.
    </p>
    <p><u><b>4. Who is considered an affiliate under Rule 144?</u></b><br>
    • Answer: An affiliate is a person who directly or indirectly controls, is controlled by, or is under common control with the issuer.
    </p>
    <p><u><b>5. How does Rule 144 work?</u></b><br>
    • Answer: Rule 144 allows holders to resell securities if specific conditions related to holding period, volume, and disclosure are met.
    </p>
    <p><u><b>6. What is the holding period requirement under Rule 144?</u></b><br>
    • Answer: Restricted securities must be held for at least 6 months for reporting companies and 12 months for non-reporting companies.
    </p>
    <p><u><b>7. Are there volume limitations under Rule 144?</u></b><br>
    • Answer: Yes, affiliates may sell only a limited number of shares during any three-month period.
    </p>
    <p><u><b>8. Are public information requirements part of Rule 144?</u></b><br>
    • Answer: Yes, adequate current public information about the issuer must be available before resale.
    </p>
    <p><u><b>9. Is a filing required under Rule 144?</u></b><br>
    • Answer: Affiliates must file Form 144 with the SEC if the sale exceeds certain thresholds.
    </p>
    <p><u><b>10. Can non-affiliates sell under Rule 144?</u></b><br>
    • Answer: Yes, non-affiliates can sell restricted securities after meeting the holding period, with fewer restrictions.
    </p>
    <p><u><b>11. Does Rule 144 remove resale restrictions entirely?</u></b><br>
    • Answer: No, it provides a safe harbor; sales outside Rule 144 may still be possible but carry legal risk.
    </p>
    <p><u><b>12. How does Rule 144 differ from Rule 144A?</u></b><br>
    • Answer: Rule 144 applies to public resales, while Rule 144A allows private resales to qualified institutional buyers (QIBs).
    </p>
    <p><u><b>13. What are the benefits of Rule 144 for investors?</u></b><br>
    • Answer: It provides a clearer path to liquidity for private equity and restricted security holders.
    </p>
    <p><u><b>14. What risks are associated with Rule 144 sales?</u></b><br>
    • Answer: Risks include compliance errors, limited liquidity, market impact, and regulatory penalties.
    </p>
    <p><u><b>15. When should investors rely on Rule 144?</u></b><br>
    • Answer: Investors should rely on Rule 144 when seeking to legally resell restricted or control securities in public markets.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def privateequitysecuritiesrule144twelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Private Equity Securities – Rule 144</b></u><br>
    Capital Type: Restricted Securities Resale Liquidity Framework</p></center>
    <p><b><u>1 – Stage of Development Assessment</b></u><br>
    Rule 144 is best suited for companies that have already issued private equity securities and have reached a later stage of development where providing limited liquidity to shareholders becomes relevant. This framework is not used for primary capital raising and typically applies to growth-stage or mature private companies, as well as public companies managing secondary liquidity. {{stage}} may align with Rule 144 liquidity planning.
    </p>
    <p><b><u>2 – Entity Type Assessment</b></u><br>
    Rule 144 transactions apply to C-Corporations that have issued restricted or control securities. LLC interests generally do not fall under Rule 144 in the same way as corporate securities, making this rule most relevant to corporate equity issuers rather than alternative entity structures. {{entity}} structure relevance varies.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</b></u><br>
    Companies utilizing Rule 144 have already raised private capital and issued restricted securities to founders, employees, or early investors. Rule 144 does not depend on capitalization levels but rather on holding periods, issuer reporting status, and shareholder classification. {{preraise}} prior capital is {{preraise}} relevant.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</b></u><br>
    Rule 144 operates within the secondary private and public securities markets, providing a regulatory safe harbor for the resale of restricted and control securities. This market facilitates liquidity events rather than new capital formation. {{premarket}} reflects {{premarket}} secondary market activity.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</b></u><br>
    Rule 144 does not involve raising new capital for the issuer. Instead, it governs the volume and conditions under which existing securities may be resold, with limits based on trading volume, outstanding shares, and regulatory thresholds. {{raisegoal}} is {{raisegoal}} applicable to Rule 144 transactions.
    </p>
    <p><b><u>6 – Capital Round Assessment</b></u><br>
    Rule 144 is not a capital round and does not constitute a financing event. It enables secondary transactions that allow existing shareholders to sell shares without registering them, provided regulatory conditions are met. {{tranch}} is {{tranch}} relevant to Rule 144.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</b></u><br>
    Sales under Rule 144 may occur over time and are often executed in tranches to comply with volume limitations and market conditions. Shareholders may stagger sales to manage price impact and regulatory compliance. {{rounds}} reflects {{rounds}} typical Rule 144 approach.
    </p>
    <p><b><u>8 – Use of Funds Assessment</b></u><br>
    Proceeds from Rule 144 sales go to selling shareholders rather than the issuing company. Funds are typically used for personal liquidity, portfolio diversification, or tax planning and do not directly support company operations. {{useoffund}} represents {{useoffund}} shareholder-level use.
    </p>
    <p><b><u>9 – Risk Assessment</b></u><br>
    Risk to buyers includes limited information availability for private companies, market liquidity risk, and resale restrictions. For issuers, risk includes potential market signaling effects and administrative compliance risk.
    </p>
    <p><b><u>10 – Capital Cost Assessment</b></u><br>
    There is no direct capital cost to the issuer, as Rule 144 does not involve new financing or dilution. Indirect costs may include administrative oversight, legal review, and potential market perception impacts. {{enterprisecost}} is {{enterprisecost}} relevant.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</b></u><br>
    Upfront costs are generally low to moderate and include legal review, compliance verification, broker fees, and administrative processing. Costs are typically borne by selling shareholders rather than the company. {{upfrontcost}} is {{upfrontcost}} typical.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</b></u><br>
    Timing to liquidity under Rule 144 depends on statutory holding periods, issuer reporting status, and market conditions. Once eligibility requirements are met, transactions can be executed relatively quickly, subject to volume and filing constraints. {{upfronttime}} reflects {{upfronttime}} Rule 144 liquidity timing.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
