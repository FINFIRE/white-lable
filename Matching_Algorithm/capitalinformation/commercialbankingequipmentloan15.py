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


def commercialbankingequipmentloan(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Commercial Banking</b></u><br>

    Capital Type: Equipment Loan </center></p>

    <p><b><u>Introduction</u></b><br>

Equipment loans are a form of commercial bank financing used by businesses to purchase machinery, vehicles, technology, or other fixed assets essential for operations. Under this financing method, the purchased equipment itself serves as collateral for the loan, reducing lender risk and enabling businesses to access capital without equity dilution. {n} fits that definition. Commercial banks widely use equipment loans to support business productivity, expansion, and modernization across industries. According to the World Bank, asset-backed lending such as equipment financing plays a critical role in improving access to credit for small and medium-sized enterprises (SMEs), particularly in capital-intensive sectors. Equipment loans typically cover 70% to 100% of the equipment cost and are repaid over the useful life of the asset. While equipment loans offer predictable repayment terms and lower interest rates than unsecured loans, they require strong creditworthiness and expose businesses to repayment obligations regardless of asset performance.  </p>

 

    <p><b><u>Definition of Capital Type</b></u><br>

    <br>1.	An equipment loan is a commercial bank loan specifically issued for the purpose of acquiring business equipment, where the financed asset itself serves as collateral. The borrower repays the loan through fixed installments over a predetermined term, usually aligned with the equipment’s economic life. Ownership of the equipment may transfer to the borrower immediately or upon loan completion, depending on loan structure. Because the loan is secured by a tangible asset, interest rates are generally lower than those for unsecured business loans (Investopedia, n.d.).²

<br>



    <br>2.	Equipment loans are best suited for established small and medium-sized businesses that require machinery or technology to support core operations. These include manufacturing firms, construction companies, transportation providers, healthcare facilities, agricultural enterprises, and service businesses requiring specialized tools or IT infrastructure. Businesses with stable cash flows, proven operating history, and clear revenue generation capacity benefit most from equipment financing. Startups may also qualify if they can demonstrate strong financial backing, industry experience, or additional collateral. Equipment loans are particularly effective when the purchased asset directly contributes to revenue generation (OECD, 2022).³

<br>


    <br>3.	Equipment financing has long been a foundational component of commercial banking, evolving alongside industrialization and mechanization in the 20th century. As businesses increasingly relied on machinery and technology to scale production, banks developed asset-backed lending models to finance capital expenditures while mitigating credit risk. In recent decades, equipment loans have expanded to include technology and digital infrastructure, reflecting changes in business operations. Financial institutions continue to refine equipment financing products to support SME competitiveness and productivity growth (International Finance Corporation, 2020).⁴

<br>

    <br>4.	Despite their advantages, equipment loans involve certain risks and limitations. Borrowers are obligated to repay the loan even if the equipment becomes obsolete, underperforms, or depreciates faster than expected. Failure to meet repayment obligations can result in repossession of the equipment and damage to business credit ratings. Additionally, banks may require down payments, personal guarantees, or strong credit profiles, limiting access for early-stage businesses. Equipment loans are also restricted to asset purchases and cannot be used for general working capital needs (Harvard Business Review, 2020).⁵

<br>

    <br>5.	To obtain an equipment loan, a business must apply through a commercial bank or financial institution and provide details about the equipment being purchased, including cost, supplier, and expected useful life. The lender evaluates the borrower’s creditworthiness, cash-flow stability, and business performance, as well as the resale value of the equipment. Upon approval, the bank disburses funds directly to the equipment supplier or reimburses the borrower. The borrower repays the loan through scheduled installments over the agreed term. Throughout the loan period, businesses must maintain insurance on the equipment and comply with loan covenants (SBA, n.d.).⁶
    </p>

                            

    <p><u><b>References</u></b><br>

    <br>Investopedia. (n.d.). Equipment financing. <a href=" https://www.investopedia.com "> https://www.investopedia.com </a>

<br>

     <br>OECD. (2022). Financing SMEs and entrepreneurs. <a href=" https://www.oecd.org"> https://www.oecd.org</a>

<br>

   <br>International Finance Corporation (IFC). (2020). SME finance and productivity.  <a href="https://www.ifc.org">https://www.ifc.org</a>

<br>

   <br>Harvard Business Review. (2020). Debt financing risks for businesses. <a href=" https://hbr.org "> https://hbr.org </a>

<br>

   <br>U.S. Small Business Administration (SBA). (n.d.). Equipment loans. <a href=" https://www.sba.gov"> https://www.sba.gov</a>

<br>


    </p>

                                                          

    <p><u><b>Legal Qualification Requirements</u></b>

<br>•	Legally registered business entity
<br>•	Valid business licenses and permits
<br>•	Acceptable business and owner credit history
<br>•	Ability to provide personal or corporate guarantees
<br>•	Insurance coverage for financed equipment
<br>•	Compliance with banking and tax regulations




    </p>

                                

    <p><b><u>Supporting Document List</u></b>
<br>•	Equipment quotation or purchase agreement
<br>•	Business registration documents
<br>•	Business and personal financial statements
<br>•	Bank statements
<br>•	Tax returns
<br>•	Cash-flow projections
<br>•	Insurance documentation
<br>•	Loan application and credit authorization forms




    </p>
        """)


    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def commercialbankingequipmentloanfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Commercial Banking<br>

    Equipment Loan</center></b></p>                       

    <p><center><u><b>Frequently Asked Question</u></b></center></p>

                            

    <p><u><b>1. What is a commercial bank equipment loan?</u></b><br>

    •Answer: A commercial bank equipment loan is a debt financing product that allows businesses to purchase or refinance equipment by borrowing funds from a bank. The equipment being purchased typically serves as collateral for the loan.
</p>

                            

     <p><u><b>2. How does an equipment loan work?</u></b><br>

    •Answer: The bank provides funds to purchase equipment, and the business repays the loan over a fixed term with interest. The equipment itself secures the loan, reducing lender risk and often resulting in lower interest rates compared to unsecured loans.
</p>


                            

    <p><u><b>3. What types of equipment can be financed?</u></b><br>

    •Answer: Equipment loans can finance machinery, vehicles, manufacturing tools, medical equipment, IT hardware, construction equipment, and other long-term, business-use assets.
</p>


                            

   <p><u><b>4. What types of businesses are best suited for equipment loans?</u></b><br>

    •Answer: Equipment loans are best suited for established startups, SMEs, and growing businesses with predictable cash flow that need physical assets to operate or expand.
</p>


                            

    <p><u><b>5. How much funding can be obtained through an equipment loan?</u></b><br>

    •Answer: Loan amounts depend on the cost and resale value of the equipment, the borrower’s credit profile, and bank policies. Many banks finance a large percentage of the equipment’s purchase price.
</p>


                            

   <p><u><b>6. How quickly can businesses access equipment loan funding?</u></b><br>

    •Answer: Funding timelines vary but are generally faster than unsecured business loans. Once approved, funds are typically disbursed directly to the equipment vendor.
</p>


                            

 <p><u><b>7. Does an equipment loan require equity dilution?</u></b><br>

    •Answer: No. Equipment loans are debt-based financing. Business owners retain full ownership and control.
</p>
                            

     <p><u><b>8. Are collateral and personal guarantees required?</u></b><br>

    •Answer: The equipment itself usually serves as collateral. Some banks may also require personal guarantees, especially for smaller or newer businesses.
</p>

                            

   <p><u><b>9. What are the interest rates and repayment terms?</u></b><br>

    •Answer: Interest rates are typically lower than unsecured loans due to collateral backing. Repayment terms often align with the useful life of the equipment and may range from short to medium-term.
</p>

                            

    <p><u><b>10. What can equipment loan funds be used for?</u></b><br>

    •Answer: Funds must be used to purchase, upgrade, or refinance business equipment. They generally cannot be used for working capital or unrelated expenses.
</p>

                        

   <p><u><b>11. What are the key benefits of equipment loans?</u></b><br>

    •Answer: Benefits include asset-backed financing, lower interest rates, predictable repayment schedules, tax advantages (such as depreciation), and preservation of working capital.
</p>

                        

  <p><u><b>12. What are the risks or limitations of equipment loans?</u></b><br>

    •Answer: Risks include repayment obligations regardless of business performance, potential obsolescence of equipment, and repossession if the loan is not repaid.
</p>

                        

   <p><u><b>13. Can equipment loans be combined with other funding sources?</u></b><br>

    •Answer: Yes. Equipment loans are often combined with working capital loans, grants, owner equity, or accelerators as part of a broader financing strategy.
</p>

                        

 <p><u><b>14. How do equipment loans compare to leasing?</u></b><br>

    •Answer: Equipment loans lead to ownership of the asset, while leasing provides usage without ownership. Loans may be better for long-term use, while leases offer flexibility and lower upfront costs.
</p>

                        

  <p><u><b>15. How can businesses improve their chances of equipment loan approval?</u></b><br>

    •Answer: Businesses can improve approval chances by maintaining good credit, demonstrating cash-flow stability, providing clear equipment details, and working with reputable vendors.
</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def commercialbankingequipmentloantwelve(request):
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

    Capital Type: Equipment Loan</p></center>

 

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Commercial equipment loans are best suited for operating and growth-stage businesses that require machinery, vehicles, or specialized equipment to support production or service delivery. They are generally not suitable for idea-stage or pre-revenue startups, as lenders require demonstrated operational stability.

    </p>

   

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Equipment loans are available to all formal business entities, including sole proprietorships, partnerships, LLCs, and corporations. Businesses must be legally registered and compliant with banking and regulatory requirements.

    </p>

   

    <p><b><u>3 - Pre Capital Assessment</b></u><br>

Lenders typically expect some level of operating history, revenue generation, and owner equity contribution. While prior funding is allowed, the business must show sufficient cash flow to service additional debt.
    </p>

 

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>

Equipment loans operate within traditional commercial debt markets. Prior equity investment does not restrict eligibility, but lenders evaluate existing debt obligations to assess overall leverage and repayment capacity.
    </p>

 

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>

The loan amount is usually tied directly to the value of the equipment being financed, often covering 70–100% of the purchase price. This makes equipment loans suitable for targeted capital needs rather than general working capital.
    </p>

   

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Equipment loans do not follow startup funding rounds. They align with asset acquisition or expansion phases, where the business is investing in productive capacity.

    </p>

 

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>

Funds are typically disbursed in a single lump sum directly to the equipment vendor. In some cases, staged payments may occur for large or custom-built equipment.
    </p>

   

    <p><b><u>8 - Use of Funds Assessment</b></u><br>

Funds are restricted to the purchase of approved equipment, such as:
<br>•	Machinery and manufacturing equipment
<br>•	Vehicles and transportation assets
<br>•	Technology and IT hardware
<br>•	Medical, construction, or industrial equipment
Use for unrelated expenses is not permitted.

    
</p>

   

    <p><b><u>9 - Risk Assessment</b></u><br>

Risk is moderate. The equipment itself serves as collateral, reducing lender risk. However, the business remains liable for repayment even if the equipment becomes obsolete or underperforms.
    </p>

 

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital is moderate, consisting of fixed or variable interest rates. Rates are generally lower than unsecured loans due to collateralization but higher than subsidized government programs.

    </p>

   

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs may include down payments, documentation fees, appraisal or inspection fees, and insurance requirements. These costs vary based on equipment type and lender policies.

    </p>

 

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>

Equipment loans typically have a moderate approval timeline, ranging from 2–6 weeks, depending on credit evaluation, equipment valuation, and documentation. Some banks offer faster approvals for standardized assets.
</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)