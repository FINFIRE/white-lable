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


def ownerdebtretirement401ksdi(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""<p><center><b><u>Definition of Capital Market: Owner Debt</b></u><br>

    Capital Type: Retirement (401K) SDI </center></p>

    <p><b><u>Introduction</u></b><br>

Retirement (401k) Self-Directed Investment (SDI)—often structured as a Rollover as Business Startup (ROBS)—is ideal for entrepreneurs seeking to use their own retirement savings as seed capital for a new or existing business. It is designed so that individuals can access their existing 401k or IRA funds without paying early withdrawal penalties or income taxes at the time of the transaction. {n} fits that definition. This funding mechanism has been a significant driver of independent business ownership since the mid-1970s. For example, in 2024, the Small Business Administration and industry experts estimated that thousands of new businesses—particularly franchises—were funded using ROBS arrangements. Unlike a 401k loan, which is capped at $50,000, a ROBS allows the owner to invest a significant portion of their retirement nest egg into their own company’s stock. On average, ROBS participants invest between **$100,000 and $500,000**, enabling them to launch debt-free and avoid the high interest rates associated with traditional commercial loans. While using retirement funds offers a non-dilutive and debt-free start, the risk of losing one's retirement savings if the business fails, coupled with strict IRS and Department of Labor (DOL) compliance requirements, makes it a high-stakes strategy for any founder.    </p>

 

    <p><b><u>Definition of Capital Type</b></u><br>

    <br>1.	Retirement (401k) SDI / ROBS is a financial arrangement that allows an entrepreneur to use their 401k, 403b, or traditional IRA funds to purchase stock in their own business. The process involves three main steps: creating a new C-Corporation, establishing a new 401k plan for that corporation, and rolling over existing retirement funds into the new plan to buy company shares. Because the transaction is a "rollover" into a new qualified plan, it is not considered a taxable distribution. (Guidant Financial, 2025)

<br>



    <br>2.	The best type of companies to raise capital via ROBS are startups or franchises that require significant upfront capital and have a high probability of generating steady cash flow. These entrepreneurs typically have at least $50,000 in a "rollable" retirement account and wish to avoid the monthly debt service of a bank loan. It is particularly well-suited for founders who plan to be "active employees" of the business, as the IRS requires participants to be bona fide employees of the C-Corp. (FranNet, 2025)

<br>


    <br>3.	The ROBS model emerged following the passage of the Employee Retirement Income Security Act (ERISA) of 1974. Specifically, Section 408(e) provided an exemption that allowed retirement plans to purchase "qualifying employer securities." While initially intended for large-scale employee stock ownership plans (ESOPs), specialized financial firms in the early 2000s began packaging this as a tool for small business startups. Since then, the IRS has issued specific guidelines (notably the 2008 ROBS Project memorandum) to ensure these plans are not used solely for tax evasion. (Internal Revenue Service, 2008)

<br>

    <br>4.	While ROBS provides debt-free capital, it carries extreme compliance risks. The IRS and DOL monitor these plans for "prohibited transactions"—such as using the funds to pay the owner's personal salary before the business is operational or failing to offer the 401k plan to other eligible employees. If the plan is found to be non-compliant, the entire rollover could be declared a taxable distribution, resulting in massive back taxes and a 10% early withdrawal penalty. Additionally, the business must be a C-Corporation, which may not be the most tax-efficient structure for every founder. (The Balance, 2024)

<br>

    <br>5.	To raise capital via a retirement rollover, a founder must work with a specialized ROBS provider to ensure legal and tax "airtightness." The founder must incorporate as a C-Corp, adopt a qualified retirement plan, and then direct the rollover. The funds must be used for legitimate business expenses, such as inventory, equipment, or working capital. Annual filings, such as IRS Form 5500, are required to maintain the plan's qualified status and avoid audits. (Catching Clouds, 2025)
    </p>

                            

    <p><u><b>References</u></b><br>

    <br>Guidant Financial. (2025). What is ROBS? A Guide to Rollovers as Business Startups.  <a href="https://www.guidantfinancial.com/financing-solutions/robs/">https://www.guidantfinancial.com/financing-solutions/robs/</a>

<br>

     <br>FranNet. (2025). Using Your 401k to Start a Business. <a href=" https://frannet.com/financing/robs/"> https://frannet.com/financing/robs/</a>

<br>

   <br>Internal Revenue Service (IRS). (2008). Rollover as Business Startups (ROBS) Compliance Project. <a href="https://www.irs.gov/retirement-plans/rollover-as-business-startups-robs-compliance-project"> https://www.irs.gov/retirement-plans/rollover-as-business-startups-robs-compliance-project</a>

<br>

   <br>The Balance. (2024, December 10). How to Use a ROBS to Fund Your Business.  <a href="https://www.thebalancemoney.com/using-a-robs-to-fund-your-business-4135246">https://www.thebalancemoney.com/using-a-robs-to-fund-your-business-4135246</a>

<br>

   <br>Catching Clouds. (2025). Tax and Accounting for ROBS C-Corporations.  <a href="https://www.catchingclouds.net/blog/robs-compliance-checklist">https://www.catchingclouds.net/blog/robs-compliance-checklist</a>

<br>


    </p>

                                                          

    <p><u><b>Legal Qualification Requirements</u></b>

<br>•	Eligible Retirement Account – Funds must be in a 401k, 403b, or Traditional IRA (Roth IRAs and "active" 401ks with current employers are generally ineligible).
<br>•	C-Corporation Structure – The business must be legally incorporated as a C-Corp to issue stock.
<br>•	Bona Fide Employee Status – The founder must be an active employee providing services to the company.
<br>•	Plan Universality – The 401k plan must be offered to all eligible employees on the same terms as the founder.
<br>•	Qualified Plan Adoption – The company must adopt a new, IRS-approved 401k plan.
<br>•	Stock Appraisal – The stock must be purchased at fair market value.
<br>•	No Prohibited Transactions – Funds cannot be used for personal expenses or to pay off pre-existing personal debt.
<br>•	Annual Filing – Commitment to filing Form 5500 with the IRS every year.




    </p>

                                

    <p><b><u>Supporting Document List</u></b>
<br>•	Articles of Incorporation – Proof of C-Corporation status.
<br>•	Retirement Account Statements – To verify the amount and eligibility of funds for rollover.
<br>•	IRS Determination Letter – Verification that the new 401k plan is "qualified."
<br>•	Stock Purchase Agreement – Documentation of the 401k plan’s purchase of company shares.
<br>•	Stock Certificates – Evidence of shares issued to the retirement plan.
<br>•	Corporate Bylaws – Governing documents of the C-Corp.
<br>•	Business Plan – Required by some ROBS providers to ensure the venture is a legitimate trade or business.
<br>•	Form 5500 – The annual return/report for the employee benefit plan (filed after the first year).




    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def ownerdebtretirement401ksdifaq(request):
    introduction = mark_safe("""<p><b><center>Capital Market: Owner Debt<br>

    Retirement (401K) SDI</center></b></p>                       

    <p><center><u><b>Frequently Asked Question</u></b></center></p>

                            

    <p><u><b>1.	What is Owner Debt using a 401K SDI, and how does it differ from other funding options? </u></b><br>

    •Answer: Owner Debt using a 401K SDI (Self-Directed Individual) allows business owners to borrow or roll over funds from their retirement accounts, such as a 401K, into their own business, providing capital while maintaining control over the investment.
</p>

                            

     <p><u><b>2.	What types of businesses are best suited for 401K SDI funding? </u></b><br>

    •Answer: Early-stage or growing businesses that require flexible funding and where the owner has a clear business plan and strong potential for ROI are ideal candidates for using 401K SDI.
</p>


                            

    <p><u><b>3.	How much funding can I access through a 401K SDI? </u></b><br>

    •Answer: Funding limits are generally up to $50,000 or 50% of the vested account balance, whichever is lower, though specific rules depend on the retirement plan provider and IRS regulations.
</p>


                            

   <p><u><b>4.	How quickly can I access funds from a 401K SDI? </u></b><br>

    •Answer: Access typically takes a few days to a few weeks, depending on plan administration, account verification, and any rollover or loan procedures.
</p>


                            

    <p><u><b>5.	What are the costs of using a 401K SDI? </u></b><br>

    •Answer: Costs may include loan interest (if applicable), administrative fees, tax implications if rules are violated, and opportunity cost of lost retirement growth.
</p>


                            

   <p><u><b>6.	Do I have to give up equity when using 401K SDI? </u></b><br>

    •Answer: No, you maintain full equity ownership in your business, but you are personally responsible for repaying the 401K loan or managing the invested funds properly.
</p>


                            

 <p><u><b>7.	Can I still raise capital from other sources while using 401K SDI? </u></b><br>

    •Answer: Yes, 401K SDI can be combined with other financing options such as angel investment, venture capital, or bank loans, as long as repayment obligations are met.
</p>
                            

     <p><u><b>8.	What are the key benefits of using 401K SDI over traditional loans or investor funding? </u></b><br>

    •Answer: Benefits include no equity dilution, flexible repayment options, faster access to capital, and leveraging your own retirement savings for business growth.
</p>

                            

   <p><u><b>9.	What resources and support can I expect when using 401K SDI? </u></b><br>

    •Answer: Support comes primarily from plan administrators, financial advisors, and compliance guidance, though business mentorship is not typically included.
</p>

                            

    <p><u><b>10.	What happens if I fail to repay or misuse the 401K SDI funds? </u></b><br>

    •Answer: Failure to comply can result in tax penalties, early withdrawal penalties, and the loan being treated as a taxable distribution by the IRS.
</p>

                        

   <p><u><b>11.	Are there any risks associated with using 401K SDI? </u></b><br>

    •Answer: Risks include loss of retirement growth, potential tax penalties, personal liability for repayment, and business risk if the investment fails.
</p>

                        

  <p><u><b>12.	How does 401K SDI compare to other owner debt or personal financing options? </u></b><br>

    •Answer: 401K SDI provides direct access to personal retirement funds with no equity loss, unlike traditional loans which may require collateral or investors who demand equity.
</p>

                        

   <p><u><b>13.	Can I use 401K SDI if I have already taken other business loans? </u></b><br>

    •Answer: Yes, but repayment obligations and IRS regulations must be carefully managed to avoid conflicts or penalties.
</p>

                        

 <p><u><b>14.	What types of businesses typically benefit most from 401K SDI funding? </u></b><br>

    •Answer: Businesses with strong revenue potential, manageable risk, and clear growth plans are most likely to benefit, particularly small businesses or startups owned by the account holder.
</p>

                        

  <p><u><b>15.	How can I increase my chances of successfully using 401K SDI for my business? </u></b><br>

    •Answer: Ensure proper plan compliance, have a detailed business plan, maintain disciplined repayment, consult financial advisors, and verify IRS rules to maximize benefits while minimizing risks.
</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def ownerdebtretirement401ksditwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Owner Debt</b></u><br>

    Capital Type: Retirement (401K) SDI</p></center>

 

    <p><b><u>1 - Stage of Development Assessment</b></u><br>

This type of financing is best suited for early-stage to growth-stage businesses, particularly those needing startup capital or expansion funding without going through traditional lenders. Ideal for founders who want to leverage personal retirement savings.
    </p>

   

    <p><b><u>2 - Entity Type Assessment</b></u><br>

Eligible entities include C-Corps, LLCs, and S-Corps. Sole proprietorships and partnerships can also use this method if structured properly. The business must be eligible to receive funds rolled over from a self-directed retirement account.
    </p>

   

    <p><b><u>3 - Pre Capital Assessment</b></u><br>

A sufficient balance in a 401(k) or other retirement account is required. Prior business funding is not a disqualifier, but personal retirement assets must be available to fund the loan.
    </p>

 

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>

This is non-market-based financing using personal retirement funds. It does not involve banks, venture capital, or public markets. Previous funding sources do not restrict eligibility.
    </p>

 

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>

The amount of capital depends on the available retirement funds, typically up to 100% of the vested balance minus any penalties or tax implications. This is suitable for small to moderate capital needs.
    </p>

   

    <p><b><u>6 - Capital Round Assessment</b></u><br>
This financing method does not align with traditional investment rounds. It is primarily owner-controlled debt, often used as a bridge or seed financing.

    </p>

 

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds can generally be accessed in a single tranche, as determined by the retirement account custodian. Some plans allow multiple withdrawals or partial rollovers under SDI rules.

    </p>

   

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Funds are typically used for:
<br>•	Startup costs
<br>•	Working capital
<br>•	Equipment or inventory purchases
<br>•	Operational expansion
Personal use is restricted, and improper use could lead to tax penalties or account disqualification.


    
</p>

   

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk is high, as the owner is using personal retirement savings. Mismanagement could result in loss of retirement funds, tax penalties, and missed long-term growth. Business failure directly impacts personal financial security.

    </p>

 

    <p><b><u>10 - Capital Cost Assessment</b></u><br>

Capital cost includes potential tax implications, opportunity cost of lost investment growth, and any fees charged by the SDI custodian. There is no interest owed to an external party, but long-term financial opportunity cost can be significant.
    </p>

   

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs include custodian fees, legal fees, and administrative costs for establishing a rollover or SDI plan. These costs are generally moderate but far lower than traditional equity or bank financing.

    </p>

 

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>

Access to funds is moderately fast, typically 2–6 weeks, depending on custodian approval, paperwork completion, and fund transfer logistics.
</p>"""

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)