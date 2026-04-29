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

def commercialbankingsblc(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Commercial Banking</b></u><br>
    Capital Type: Standby Letter of Credit (SBLC) </center></p>
    <p><b><u>Introduction</u></b><br>
A Standby Letter of Credit (SBLC) is a financial guarantee issued by a commercial bank on behalf of a business to assure payment or performance obligations in the event the applicant fails to meet contractual commitments. Unlike traditional loans, an SBLC does not provide immediate cash but serves as a credit enhancement tool that strengthens trust between contracting parties. {n} fits that definition. SBLCs are widely used in domestic and international trade, infrastructure projects, leasing arrangements, and large commercial contracts where counterparty risk must be mitigated. According to the International Chamber of Commerce (ICC), standby letters of credit play a critical role in facilitating commerce by providing a secure and internationally recognized payment assurance mechanism. While SBLCs reduce counterparty risk and improve contract credibility, they require strong creditworthiness and can expose businesses to contingent liabilities.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.A Standby Letter of Credit is a legally binding undertaking issued by a bank, committing to pay a specified beneficiary if the applicant fails to fulfill a contractual or financial obligation. SBLCs function as secondary payment mechanisms, activated only upon default or non-performance by the applicant. Unlike documentary letters of credit used for routine trade payments, SBLCs are contingent instruments and are governed by international rules such as the ICC's ISP98 or UCP 600, depending on contract terms. (ICC, n.d.)
<br>


    <br>2.  SBLCs are best suited for established businesses engaged in large-scale commercial transactions, infrastructure projects, government contracts, international trade, or long-term supply agreements. These instruments are commonly used by construction firms, exporters and importers, energy companies, real estate developers, and manufacturing enterprises. Companies with strong financial standing, stable cash flows, and proven performance history benefit most from SBLCs, as banks assess creditworthiness before issuance. (World Bank, 2021)
<br>

    <br>3. The use of standby letters of credit expanded significantly during the latter half of the 20th century alongside globalization and growth in cross-border trade. Initially developed in the United States as an alternative to bank guarantees, SBLCs gained international acceptance due to their standardized structure and enforceability. Over time, SBLCs became governed by internationally recognized frameworks such as the ICC's Uniform Customs and Practice (UCP) and later the International Standby Practices (ISP98), enhancing legal certainty and global adoption. (ICC, 2020)
<br>
    <br>4.Despite their benefits, SBLCs involve several risks and limitations. Issuing an SBLC creates a contingent liability for the applicant, which may impact borrowing capacity and balance sheet ratios. Banks typically require collateral, cash margins, or counter-guarantees, increasing capital commitment. Improper documentation or ambiguous contract terms can lead to disputes or wrongful draws. Additionally, fees for issuance, renewal, and amendment can be significant over long durations. (Harvard Business Review, 2019)
<br>
    <br>5.
To obtain an SBLC, a business must apply through a commercial bank and provide detailed information regarding the underlying contract, beneficiary, amount, and duration. The bank conducts credit assessment, risk analysis, and due diligence before approval. Once issued, the SBLC is delivered to the beneficiary and remains valid for the agreed term. If the applicant defaults, the beneficiary may present a compliant demand for payment. Applicants must maintain collateral arrangements and comply with bank covenants throughout the SBLC's validity period. (Investopedia, n.d.)
    </p>

    <p><u><b>References</u></b><br>
    <br>International Chamber of Commerce (ICC). (n.d.). International Standby Practices (ISP98). <a href="https://iccwbo.org">https://iccwbo.org</a>
<br>
    <br>World Bank. (2021). Trade finance and risk mitigation. <a href="https://www.worldbank.org">https://www.worldbank.org</a>
<br>
    <br>International Chamber of Commerce (ICC). (2020). Uniform Customs and Practice for Documentary Credits. <a href="https://iccwbo.org">https://iccwbo.org</a>
<br>
    <br>Harvard Business Review. (2019). Managing financial risk in commercial contracts. <a href="https://hbr.org">https://hbr.org</a>
<br>
    <br>Investopedia. (n.d.). Standby letter of credit (SBLC). <a href="https://www.investopedia.com">https://www.investopedia.com</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Legally registered business entity
<br>•   Strong credit profile and banking relationship
<br>•   Underlying commercial contract requiring guarantee
<br>•   Ability to provide collateral or cash margin
<br>•   Compliance with banking, trade, and AML regulations
<br>•   No unresolved legal or financial disputes


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   SBLC application form
<br>•   Underlying contract or agreement
<br>•   Business registration documents
<br>•   Financial statements and bank statements
<br>•   Collateral or margin documentation
<br>•   Board resolution authorizing SBLC issuance
<br>•   Identification documents for compliance (KYC)

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def commercialbankingsblcfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Commercial Banking<br>
    Standby Letter of Credit (SBLC)</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is a Standby Letter of Credit (SBLC)?</u></b><br>
    •Answer: A Standby Letter of Credit (SBLC) is a bank-issued financial guarantee that assures a beneficiary that payment will be made if the applicant fails to meet contractual or financial obligations. It is commonly used as a credit enhancement or risk mitigation tool rather than a direct funding source.
</p>

    <p><u><b>2. How does an SBLC work?</u></b><br>
    •Answer: A bank issues an SBLC on behalf of its customer in favor of a beneficiary. If the customer defaults or fails to perform as agreed, the beneficiary can draw on the SBLC, and the bank pays according to the terms. The customer is then obligated to reimburse the bank.
</p>

    <p><u><b>3. How does an SBLC differ from a loan?</u></b><br>
    •Answer: An SBLC does not provide upfront cash to the business. Instead, it serves as a guarantee of payment or performance. Funds are only paid if the SBLC is called due to default or non-performance.
</p>

    <p><u><b>4. What types of businesses commonly use SBLCs?</u></b><br>
    •Answer: SBLCs are commonly used by medium to large businesses engaged in international trade, construction, infrastructure projects, leasing, energy, manufacturing, and government contracts where performance or payment assurance is required.
</p>

    <p><u><b>5. What are typical uses of an SBLC?</u></b><br>
    •Answer: SBLCs are used to secure contracts, support trade transactions, guarantee lease payments, backstop loans, meet regulatory requirements, or enhance creditworthiness in commercial agreements.
</p>

    <p><u><b>6. Does an SBLC require collateral?</u></b><br>
    •Answer: Yes. Banks usually require collateral, cash margin, or strong creditworthiness before issuing an SBLC. Collateral requirements depend on the applicant's financial strength and the SBLC amount.
</p>

    <p><u><b>7. Does an SBLC involve equity dilution?</u></b><br>
    •Answer: No. An SBLC is a non-dilutive, debt-related instrument. It does not affect ownership or control of the business.
</p>

    <p><u><b>8. How much does an SBLC cost?</u></b><br>
    •Answer: Costs typically include issuance fees, annual commitment fees, and bank charges. Fees are usually expressed as a percentage of the SBLC amount and depend on risk, duration, and collateral provided.
</p>

    <p><u><b>9. How long is an SBLC valid?</u></b><br>
    •Answer: SBLCs are issued for a defined term, often ranging from several months to multiple years, depending on the underlying obligation or contract.
</p>

    <p><u><b>10. What happens if an SBLC is drawn?</u></b><br>
    •Answer: If the beneficiary draws on the SBLC, the bank pays the amount specified and then seeks reimbursement from the applicant. This may convert into a loan or immediate repayment obligation for the business.
</p>

    <p><u><b>11. What are the benefits of using an SBLC?</u></b><br>
    •Answer: Benefits include enhanced credibility, risk mitigation for counterparties, ability to secure contracts without upfront cash, and support for large or complex commercial transactions.
</p>

    <p><u><b>12. What are the risks or limitations of an SBLC?</u></b><br>
    •Answer: Risks include potential cash flow strain if the SBLC is called, collateral requirements, fees, and increased liability exposure. SBLCs do not provide working capital.
</p>

    <p><u><b>13. Can an SBLC be combined with other financing instruments?</u></b><br>
    •Answer: Yes. SBLCs are often used alongside loans, trade finance, equipment financing, or project financing to strengthen overall deal structures.
</p>

    <p><u><b>14. How does an SBLC compare to a bank guarantee?</u></b><br>
    •Answer: An SBLC functions similarly to a bank guarantee, but SBLCs are more commonly used in international trade and follow standardized international rules, making them widely accepted across borders.
</p>

    <p><u><b>15. How can businesses improve their chances of SBLC approval?</u></b><br>
    •Answer: Businesses can improve approval chances by maintaining strong credit profiles, providing adequate collateral, demonstrating contract viability, and working with established banking partners.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def commercialbankingsblctwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Commercial Banking</b></u><br>
    Capital Type: Standby Letter of Credit (SBLC)</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Standby Letters of Credit are best suited for operating and established businesses involved in trade, contracts, infrastructure, or large commercial transactions. SBLCs are not appropriate for early-stage or pre-revenue startups, as banks require strong financial standing and credibility.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
SBLCs are available to formally registered business entities, including corporations, LLCs, partnerships, and established sole proprietorships. The applicant must have an existing banking relationship and verifiable financial history.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Applicants must demonstrate strong financial capacity, including sufficient cash balances, assets, or credit lines. Banks often require collateral or cash margin before issuing an SBLC.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
SBLCs operate within traditional commercial banking markets. Prior equity or debt financing does not disqualify applicants, but banks evaluate overall leverage and credit exposure before approval.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
An SBLC does not provide direct funding. Instead, it guarantees payment to a third party if contractual obligations are not met. SBLC amounts depend on the contract value being secured rather than capital needs.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
SBLCs do not align with startup funding rounds. They support transactional or contract-based financing stages, such as bidding, procurement, trade execution, or project delivery.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
There is no tranche disbursement, as funds are only drawn if the applicant defaults. The SBLC remains contingent throughout its validity period.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
SBLCs are used to:
<br>•   Secure trade and supply contracts
<br>•   Support tender or bid requirements
<br>•   Guarantee lease or rental agreements
<br>•   Back performance or payment obligations
They cannot be used as working capital unless drawn due to default.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk is moderate to high. If the SBLC is called, the bank will seek immediate reimbursement from the applicant, potentially impacting cash flow and credit standing. Reputational risk also exists if obligations are not met.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of an SBLC includes issuance fees, annual renewal fees, and collateral opportunity costs. While there is no interest unless drawn, total costs can be significant for long-term or high-value guarantees.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs include bank fees, collateral requirements, legal documentation, and margin deposits. These costs vary based on risk profile, bank policy, and SBLC size.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
SBLC issuance typically takes 1-4 weeks, depending on credit evaluation, collateral arrangement, and documentation. Renewal or amendment timelines may be shorter for existing clients.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
