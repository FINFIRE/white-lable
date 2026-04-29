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


def commercialbankingacquisitionloan(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Commercial Banking</b></u><br>

    Capital Type: Acquisition Loan </center></p>

    <p><b><u>Introduction</u></b><br>

An Acquisition Loan is ideal for companies seeking to purchase an existing business, a competitor, or a franchise. It is designed so that financial institutions can provide the necessary leverage to facilitate ownership transitions, allowing privately held enterprises to achieve rapid growth through inorganic expansion rather than organic development alone. {n} fits that definition. Business acquisitions are a primary driver of market consolidation and wealth transfer. In 2024, the "Silver Tsunami"—the retirement of Baby Boomer business owners—fueled a record number of acquisition loans globally. Lenders like Live Oak Bank and Huntington National Bank specialize in these transactions, often utilizing SBA enhancements to bridge collateral gaps. On average, acquisition loans cover 70% to 90% of the purchase price, with loan amounts ranging from $250,000 to over $10 million, typically amortized over 7 to 10 years. While acquisition loans offer a fast track to scaling, the risks of "overpaying" (goodwill risk), cultural integration failures, and the significant debt service burden on the newly combined entity require rigorous pre-loan due diligence.    </p>

 

    <p><b><u>Definition of Capital Type</b></u><br>

    <br>1.	An Acquisition Loan is a debt instrument specifically earmarked for the purchase of a company’s assets or stock. Unlike a standard working capital loan, the underwriting is heavily focused on the historical cash flow of the target company. The "Debt Service Coverage Ratio" (DSCR) is calculated based on the target's ability to pay back the loan from its ongoing operations. (Investopedia, 2025)

<br>



    <br>2.	The best type of companies to raise an acquisition loan are established businesses looking to "bolt-on" a competitor or individuals with significant industry experience seeking to buy a profitable "turnkey" operation. Lenders prefer targets with clean financial records, a diverse customer base, and "sticky" recurring revenue. Franchises are also prime candidates due to their proven, replicable business models. (Forbes Advisor, 2025)

<br>


    <br>3.	Acquisition lending emerged as a specialized field alongside the leveraged buyout (LBO) boom of the 1980s. While LBOs were once associated with "corporate raiding," the modern acquisition loan market is largely focused on "Small to Medium Enterprise" (SME) transitions. Since 2023, there has been a significant shift toward "Seller-Carried Portions," where banks require the seller to hold a secondary note to ensure a smooth transition and skin in the game. (Harvard Business Review, 2024)

<br>

    <br>4.	While acquisition loans facilitate growth, they carry "integration and valuation" risks. If the buyer fails to retain key employees or customers post-sale, the cash flow can drop, leading to a default. There is also the risk of Goodwill Impairment, where the intangible value of the brand or customer list is found to be worth less than the loan amount. Most banks mitigate this by requiring a third-party business valuation before funding. (BizBuySell, 2025)

<br>

    <br>5.	To raise an acquisition loan, the borrower must present a "Quality of Earnings" report and a detailed transition plan. Lenders look for "Global Cash Flow," which combines the income of the buyer and the target. A key requirement is often the "Equity Injection"—the buyer must typically provide 10% to 25% of the purchase price in cash to prove commitment and reduce the bank's risk exposure. (J.P. Morgan, 2025)
    </p>

                            

    <p><u><b>References</u></b><br>

    <br>Investopedia. (2025, May 19). Acquisition Loan: Definition and How It Works.  <a href="https://www.investopedia.com/terms/a/acquisition-loan.asp">https://www.investopedia.com/terms/a/acquisition-loan.asp</a>

<br>

     <br>Forbes Advisor. (2025, February 11). Business Acquisition Loans: Best Options For 2025.  <a href="https://www.forbes.com/advisor/business-loans/business-acquisition-loans/">https://www.forbes.com/advisor/business-loans/business-acquisition-loans/</a>

<br>

   <br>Harvard Business Review. (2024). How to Finance a Small Business Acquisition.  <a href="https://hbr.org/2024/03/how-to-finance-a-small-business-acquisition">https://hbr.org/2024/03/how-to-finance-a-small-business-acquisition</a>

<br>

   <br>BizBuySell. (2025). Financing the Purchase of a Business.  <a href="https://www.bizbuysell.com/guide/financing-the-purchase/">https://www.bizbuysell.com/guide/financing-the-purchase/</a>

<br>

   <br>J.P. Morgan. (2025). Business Acquisition Financing Options.  <a href="https://www.jpmorgan.com/insights/banking/business-loans/business-acquisition-financing">https://www.jpmorgan.com/insights/banking/business-loans/business-acquisition-financing</a>

<br>


    </p>

                                                          

    <p><u><b>Legal Qualification Requirements</u></b>

<br>•	Purchase Agreement – A fully executed Asset Purchase Agreement (APA) or Stock Purchase Agreement (SPA).
<br>•	Experience Requirement – The buyer must often demonstrate "management experience" in the same or a similar industry.
<br>•	Minimum Equity Injection – A cash down payment typically ranging from 10% to 20%.
<br>•	Debt Service Coverage Ratio (DSCR) – Usually requires a minimum of 1.25x based on the target company's historical EBITDA.
<br>•	Seller Note Subordination – If the seller is providing financing, the bank will require that the seller's debt is secondary to the bank's loan.
<br>•	Non-Compete Agreement – The seller must sign a legal agreement not to compete with the business for a specific period (usually 3–5 years).
<br>•	Personal Guarantee – Generally required for all owners with more than 20% equity in the acquiring entity.




    </p>

                                

    <p><b><u>Supporting Document List</u></b>
<br>•	Target’s Financials – Last 3 years of federal tax returns and year-to-date P&L and Balance Sheet.
<br>•	Quality of Earnings (QofE) Report – An independent analysis of the target’s financial health.
<br>•	Business Valuation – A certified third-party appraisal of what the business is actually worth.
<br>•	Interim Financials (Buyer & Target) – Recent performance data within the last 60 days.
<br>•	Personal Financial Statement (PFS) – For the buyer(s) to show net worth and liquidity.
<br>•	Transition Plan – A narrative describing how the buyer will manage the company post-closing.
<br>•	Source of Funds – Proof of where the down payment (equity injection) is coming from.
<br>•	Seller’s "Post-Closing" Role – A consulting or employment agreement if the seller is staying on temporarily.




    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def commercialbankingacquisitionloanfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Commercial Banking<br>

    Acquisition Loan</center></b></p>                       

    <p><center><u><b>Frequently Asked Question</u></b></center></p>

                            

    <p><u><b>1.	What is a commercial banking acquisition loan? </u></b><br>

    •Answer: A commercial banking acquisition loan is a debt financing product provided by banks to help businesses acquire another company, business unit, or significant assets, with repayment made through scheduled principal and interest payments over a fixed term.
</p>

                            

     <p><u><b>2.	What types of businesses are best suited for an acquisition loan? </u></b><br>

    •Answer: Established businesses with stable cash flows, strong financial statements, and experienced management teams are best suited, especially those seeking to grow through mergers or acquisitions.
</p>


                            

    <p><u><b>3.	What can an acquisition loan be used for? </u></b><br>

    •Answer: Acquisition loans can be used to purchase an existing business, acquire a competitor, buy out partners or shareholders, or acquire specific assets such as equipment, intellectual property, or real estate tied to a business.
</p>


                            

   <p><u><b>4.	How much funding can I receive through an acquisition loan? </u></b><br>

    •Answer: Funding amounts vary widely but typically range from hundreds of thousands to several million dollars, depending on the borrower’s creditworthiness, cash flow, collateral, and the value of the acquisition.
</p>


                            

    <p><u><b>5.	How quickly can I access funds from an acquisition loan? </u></b><br>

    •Answer: The process usually takes 30 to 90 days, as banks require due diligence, financial analysis, valuation of the target company, and legal documentation before disbursing funds.
</p>


                            

   <p><u><b>6.	What are the interest rates on acquisition loans? </u></b><br>

    •Answer: Interest rates are typically based on market benchmarks (such as prime or SOFR) plus a margin, and they vary depending on the borrower’s risk profile, loan term, and collateral offered.
</p>


                            

 <p><u><b>7.	Do acquisition loans require collateral? </u></b><br>

    •Answer: Yes, most acquisition loans require collateral, which may include business assets, acquired company assets, real estate, or personal guarantees from business owners.
</p>
                            

     <p><u><b>8.	What is the typical repayment term for an acquisition loan? </u></b><br>

    •Answer: Repayment terms generally range from 5 to 10 years, although terms may be longer if real estate is included in the acquisition.
</p>

                            

   <p><u><b>9.	Can startups qualify for commercial acquisition loans? </u></b><br>

    •Answer: Startups rarely qualify on their own, but they may be eligible if backed by strong guarantors, significant collateral, or if the acquired business has a solid operating history and cash flow.
</p>

                            

    <p><u><b>10.	What financial documents are required to apply for an acquisition loan? </u></b><br>

    •Answer: Banks typically require historical financial statements, cash flow projections, tax returns, details of the acquisition target, valuation reports, and a clear acquisition strategy.
</p>

                        

   <p><u><b>11.	Can I combine an acquisition loan with other financing sources? </u></b><br>

    •Answer: Yes, acquisition loans are often combined with owner equity, seller financing, SBA loans, or mezzanine financing to reduce risk and improve deal structure.
</p>

                        

  <p><u><b>12.	What are the main benefits of using a commercial bank acquisition loan? </u></b><br>

    •Answer: Benefits include retaining ownership control (no equity dilution), predictable repayment terms, access to larger capital amounts, and the ability to leverage acquisitions for growth.
</p>

                        

   <p><u><b>13.	What risks are associated with acquisition loans? </u></b><br>

    •Answer: Risks include increased debt burden, integration challenges, cash flow strain if the acquisition underperforms, and potential loss of collateral in case of default.
</p>

                        

 <p><u><b>14.	How does an acquisition loan differ from SBA acquisition financing? </u></b><br>

    •Answer: Commercial bank acquisition loans often have stricter requirements but faster decision-making, while SBA-backed acquisition loans may offer longer terms and lower down payments with additional government guarantees.
</p>

                        

  <p><u><b>15.	How can I improve my chances of approval for an acquisition loan? </u></b><br>

    •Answer: You can improve approval chances by demonstrating strong cash flow, providing a detailed acquisition plan, showing management experience, maintaining good credit, and contributing sufficient equity to the deal.
</p>    
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def commercialbankingacquisitionloantwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Commercial Banking
</b></u><br>

    Capital Type: Acquisition Loan</p></center>

 

    <p><b><u>1 - Stage of Development Assessment</b></u><br>

Commercial acquisition loans are best suited for established businesses or buyers acquiring an existing operating company. The target business should have a proven operating history, stable cash flows, and documented financial performance.
    </p>

   

    <p><b><u>2 - Entity Type Assessment</b></u><br>

Eligible entities typically include C-Corps, LLCs, and S-Corps. Sole proprietorships and partnerships may qualify if properly structured, but lenders generally prefer formal entities that clearly separate ownership and liability.
    </p>

   

    <p><b><u>3 - Pre Capital Assessment</b></u><br>

Borrowers are usually expected to have some level of owner equity or down payment, often ranging from 10% to 30% of the purchase price. Prior business ownership or management experience strengthens eligibility.
    </p>

 

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>

This financing operates within the private debt market through commercial banks. Existing debt obligations, credit history, and prior financing structures are carefully reviewed during underwriting.
    </p>

 

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>

Acquisition loans are designed to fund a significant portion of the purchase price, often ranging from hundreds of thousands to several million dollars, depending on business valuation, cash flow, and collateral.
    </p>

   

    <p><b><u>6 - Capital Round Assessment</b></u><br>

This is not a traditional equity round. The capital is structured as senior debt, sometimes combined with seller financing or mezzanine capital to complete the acquisition.
    </p>

 

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>

Funds are typically disbursed in a single tranche at closing, once all conditions are met, including due diligence, legal documentation, and regulatory approvals.
    </p>

   

    <p><b><u>8 - Use of Funds Assessment</b></u><br>

Loan proceeds are strictly used for:
<br>•	Purchasing business assets or equity
<br>•	Covering acquisition-related costs
<br>•	Refinancing seller debt (if approved)
Use of funds is tightly restricted by the loan agreement.

    
</p>

   

    <p><b><u>9 - Risk Assessment</b></u><br>

Risk is moderate, as repayment depends on the acquired company’s future performance. Integration risk, market changes, and management execution are key concerns for both lender and borrower.
    </p>

 

    <p><b><u>10 - Capital Cost Assessment</b></u><br>

Capital cost includes interest payments, fees, and potential collateral requirements. Rates depend on credit strength, loan structure, and market conditions. No equity dilution occurs, but personal guarantees are common.
    </p>

   

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>

Upfront costs can be moderate to high, including legal fees, valuation costs, due diligence expenses, and bank origination fees.
    </p>

 

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>

The timeline to funding is typically 60–120 days, depending on deal complexity, due diligence requirements, and lender approval processes.
</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)