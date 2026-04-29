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
def investmentbankingbrokerdealerrepresentation(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Investment Banking</b></u><br>
    Capital Type: Broker Dealer Representation </center></p>
    <p><b><u>Introduction</u></b><br>
Investment Banking - Broker Dealer Representation refers to the process where investment banks act as brokers and dealers to facilitate capital raises through securities offerings. This involves representing a company in transactions to raise capital by offering securities such as stocks or bonds to investors. The investment bank provides advisory services, underwriting support, and market access to help the company achieve its capital raising objectives.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.Definition of Broker Dealer Representation
Broker dealer representation in investment banking involves an intermediary institution assisting companies in raising capital by facilitating the sale of securities. The broker-dealer may act as principal (dealer) or agent (broker) in the transaction, regulated by the SEC and FINRA to ensure market integrity and investor protection.
<br>


    <br>2.  Best Type of Companies
Companies with established operations, revenue history, and growth potential seeking significant capital for expansion are best suited for broker dealer representation. Minimum revenue thresholds typically apply, and companies must meet SEC/FINRA qualification standards.
<br>

    <br>3. Historical Development
Investment banking evolved from merchant banking practices in the 19th century. Modern broker-dealer representation emerged after the Securities Act of 1933 and the Securities Exchange Act of 1934, which established regulatory frameworks for capital markets.
<br>
    <br>4.Risks and Limitations
Risks include market volatility, regulatory compliance burdens, and the need for extensive disclosure and documentation. Timing of offerings and market conditions significantly impact success.
<br>
    <br>5.
Process
Companies work with investment bankers to prepare financial statements, regulatory filings, prospectuses, and marketing materials. Following SEC approval, securities are offered to qualified investors through registered broker-dealers.
    </p>

    <p><u><b>References</u></b><br>
    <br>SEC. (n.d.). Rules and regulations. <a href="https://www.sec.gov">https://www.sec.gov</a>
<br>
    <br>FINRA. (n.d.). Regulatory framework. <a href="https://www.finra.org">https://www.finra.org</a>
<br>
    <br>Harvard Law School. (n.d.). Securities law overview. <a href=""></a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   SEC Registration or Exemption
<br>•   FINRA Compliance
<br>•   AML/KYC Requirements
<br>•   Financial Statement Audit
<br>•   Disclosure Obligations


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Private Placement Memorandum
<br>•   Engagement Letter
<br>•   Audited Financial Statements
<br>•   SEC Filings
<br>•   Investor Presentations

    </p>
        """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def investmentbankingbrokerdealerrepresentationfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Investment Banking<br>
    Broker Dealer Representation</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is broker dealer representation in investment banking?</u></b><br>
    •Answer: Broker dealer representation involves investment banks acting as intermediaries to facilitate capital raises through the sale of securities (stocks or bonds). They provide advisory, underwriting, and market access services.
</p>

    <p><u><b>2. What types of companies use broker dealer representation?</u></b><br>
    •Answer: Established companies with 3+ years of operations, proven revenue, and growth potential seeking significant capital ($10M+).
</p>

    <p><u><b>3. What is the typical cost of broker dealer services?</u></b><br>
    •Answer: Costs include underwriting fees (3-8%), legal/accounting services ($500K-$5M+), and regulatory compliance expenses.
</p>

    <p><u><b>4. How long does the broker dealer process take?</u></b><br>
    •Answer: 6-12 months for registered offerings, 3-6 months for expedited processes.
</p>

    <p><u><b>5. Do I need SEC registration?</u></b><br>
    •Answer: Yes, unless an exemption applies. Most broker dealer transactions require SEC registration or Regulation D exemptions.
</p>

    <p><u><b>6. What regulatory agencies oversee this process?</u></b><br>
    •Answer: SEC (Securities and Exchange Commission) and FINRA (Financial Industry Regulatory Authority).
</p>

    <p><u><b>7. What documentation is required?</u></b><br>
    •Answer: Audited financial statements, prospectus/PPM, SEC filings, investor presentations, and legal documentation.
</p>

    <p><u><b>8. Can I restrict who buys my securities?</u></b><br>
    •Answer: Depends on the offering type. Registered offerings are unlimited; Reg D is limited to accredited investors.
</p>

    <p><u><b>9. What are the risks?</u></b><br>
    •Answer: Market volatility, timing risk, regulatory changes, and investor demand variability.
</p>

    <p><u><b>10. How much capital can I raise?</u></b><br>
    •Answer: Typically $10M-$500M+ depending on company profile and market conditions.
</p>

    <p><u><b>11. Will I lose control of my company?</u></b><br>
    •Answer: Depends on shares issued. Typically you retain control if selling minority stake.
</p>

    <p><u><b>12. What is underwriting?</u></b><br>
    •Answer: Investment bank commits to purchasing unsold securities to guarantee capital amount.
</p>

    <p><u><b>13. Can I negotiate fees?</u></b><br>
    •Answer: Yes, fee structure is negotiable based on deal complexity and market conditions.
</p>

    <p><u><b>14. What happens after the offering?</u></b><br>
    •Answer: Company becomes subject to ongoing SEC reporting, auditing, and corporate governance requirements.
</p>

    <p><u><b>15. How do I choose an investment bank?</u></b><br>
    •Answer: Based on industry expertise, track record, proposed fees, and quality of advisory team.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def investmentbankingbrokerdealerrepresentationtwelve(request):
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
    Capital Type: Broker Dealer Representation</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
This capital type suits established companies (3+ years operation) with proven revenue, operational infrastructure, and growth potential requiring significant capital deployment.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Must be legally registered corporation, LLC, or equivalent. Sole proprietorships and partnerships are generally ineligible. Must have proper corporate governance structure.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Requires demonstrated funding history. Previous capital raises, profitability, or significant revenue preferred. Bootstrap-only companies typically ineligible.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Typically accessed after private equity rounds or debt financing. Market-based transactions with SEC/FINRA oversight.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Typical range: $10 million to $500 million+. Minimum thresholds apply; smaller raises inefficient in this market.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Aligned with secondary offerings, registered direct offerings, or follow-on public offerings. Post-Series C/D stage.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Full capital deployed upon closing. May include tranches for earnouts or contingent consideration.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Restricted to disclosed purposes: working capital, acquisitions, expansion, debt repayment, or other material business objectives.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Significant market risk due to securities registration and public disclosure requirements. Subject to market conditions and investor sentiment.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
Moderate to high: underwriting fees (3-8%), legal/accounting costs, ongoing compliance obligations.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Substantial: $500K-$5M+ for due diligence, legal, accounting, registration, and marketing.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
6-12 months for registered offerings; 3-6 months for expedited processes. Regulatory approval required.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
