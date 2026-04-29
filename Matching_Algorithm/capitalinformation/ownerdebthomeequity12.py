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


def ownerdebthomeequity(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Owner Debt</b></u><br>

    Capital Type: Home Equity </center></p>

    <p><b><u>Introduction</u></b><br>

Owner debt through home equity refers to capital raised by a business owner by borrowing against the equity in their personally owned residential property. This form of financing allows entrepreneurs to access relatively low-cost capital by leveraging real estate assets rather than business assets or external investors. {n} fits that definition. Home equity financing is commonly accessed through home equity loans or home equity lines of credit (HELOCs), both of which are widely used by small business owners to fund startups, expansion, or working capital needs. According to the U.S. Federal Reserve, home equity borrowing has historically been one of the most affordable sources of debt financing due to lower interest rates compared to unsecured loans (Federal Reserve, 2022). While this method provides access to significant capital without equity dilution, it exposes the owner’s personal residence to financial risk if the business underperforms.    </p>

 

    <p><b><u>Definition of Capital Type</b></u><br>

    <br>1.	Home equity financing as owner debt involves borrowing funds secured against the market value of a homeowner’s primary residence or real estate property. The loan amount is based on the difference between the property’s current market value and the outstanding mortgage balance, known as home equity. Business owners may access this capital through a lump-sum home equity loan or a revolving HELOC. Although the funds are used for business purposes, the debt remains a personal obligation of the owner and is secured by residential property rather than the business itself (Investopedia, n.d.).

<br>



    <br>2.	Home equity–based owner debt is best suited for early-stage startups, sole proprietorships, and closely held businesses where founders have substantial home equity and limited access to traditional business financing. This method is commonly used by service-based businesses, retail ventures, and small manufacturing or trading firms that require moderate startup or expansion capital. It is most appropriate for businesses with predictable cash flows and owners who have strong personal financial stability, as repayment obligations are fixed regardless of business performance. Entrepreneurs seeking rapid access to capital without ownership dilution often consider home equity financing as a bridge or seed-stage funding option (SBA, n.d.).

<br>


    <br>3.	The use of home equity as a financing source expanded significantly in the late 20th century with the growth of consumer mortgage markets and homeownership. During periods of economic expansion, homeowners increasingly leveraged rising property values to finance small businesses and entrepreneurial ventures. Following the 2008 global financial crisis, regulatory tightening reduced excessive home equity borrowing, but the practice remained a common funding source for entrepreneurs with strong credit profiles. In recent years, rising real estate values in many regions have renewed interest in home equity as an alternative to higher-cost business loans (OECD, 2021).

<br>

    <br>4.	Despite its advantages, home equity financing carries substantial risks. The most significant risk is the potential loss of the owner’s home if loan repayments cannot be met. Unlike business loans, lenders can foreclose on personal property regardless of business structure. Additionally, using home equity increases personal financial leverage and may reduce long-term household financial security. Interest rates on HELOCs may be variable, exposing borrowers to rate fluctuations. This form of owner debt is also inaccessible to founders without property ownership or sufficient equity, limiting its applicability (Harvard Business Review, 2020).

<br>

    <br>5.	To use home equity for business financing, the owner must first apply for a home equity loan or HELOC through a financial institution. Approval is based on property valuation, creditworthiness, income stability, and existing mortgage obligations. Once funds are approved and disbursed, it is recommended that the owner formally document the transfer as an owner loan to the business and deposit funds into a business account. Proper accounting treatment, repayment tracking, and tax compliance are essential to maintain financial transparency and credibility for future financing (IRS, n.d.).
    </p>

                            

    <p><u><b>References</u></b><br>

    <br>Federal Reserve. (2022). Household debt and credit report. <a href=" https://www.federalreserve.gov"> https://www.federalreserve.gov</a>

<br>

     <br>Investopedia. (n.d.). Home equity loan and HELOC. <a href=" https://www.investopedia.com "> https://www.investopedia.com </a>

<br>

   <br>U.S. Small Business Administration (SBA). (n.d.). Financing your small business.  <a href="https://www.sba.gov">https://www.sba.gov</a>

<br>

   <br>OECD. (2021). Entrepreneurship and access to finance. <a href=" https://www.oecd.org"> https://www.oecd.org</a>

<br>

   <br>Harvard Business Review. (2020). The personal risks entrepreneurs take. <a href=" https://hbr.org "> https://hbr.org </a>

<br>Internal Revenue Service (IRS). (n.d.). Home equity loan interest and tax rules.  <a href="https://www.irs.gov">https://www.irs.gov</a>
<br>

    </p>

                                                          

    <p><u><b>Legal Qualification Requirements</u></b>

<br>•	Legal ownership of residential property
<br>•	Sufficient home equity available
<br>•	Creditworthiness and income verification
<br>•	Legal authority to borrow against property
<br>•	Proper documentation of owner loan to business
<br>•	Compliance with tax and reporting regulations



    </p>

                                

    <p><b><u>Supporting Document List</u></b>
<br>•	Property ownership documents
<br>•	Mortgage and outstanding loan statements
<br>•	Property valuation report
<br>•	Home equity loan or HELOC agreement
<br>•	Proof of fund disbursement
<br>•	Business bank deposit records
<br>•	Owner loan agreement
<br>•	Financial projections showing repayment capacity



    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def ownerdebthomeequityfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Owner Debt<br>

    Home Equity</center></b></p>                       

    <p><center><u><b>Frequently Asked Question</u></b></center></p>

                            

    <p><u><b>1. What is owner debt using home equity?</u></b><br>

    •Answer: Owner debt using home equity refers to financing a business by borrowing against the equity in a personally owned home, typically through a home equity loan or home equity line of credit (HELOC). The borrowed funds are then injected into the business as an owner loan.
</p>

                            

     <p><u><b>2. How does home equity financing work?</u></b><br>

    •Answer: Home equity financing allows homeowners to borrow based on the difference between the home’s market value and the outstanding mortgage. The owner uses these funds to support the business, creating a debt obligation rather than equity.
</p>


                            

    <p><u><b>3. How does this differ from traditional business loans?</u></b><br>

    •Answer: Unlike business loans, home equity financing is secured by personal property rather than business assets. Approval is based on the homeowner’s creditworthiness and property value, not the business’s financial history.
</p>


                            

   <p><u><b>4. What types of businesses are best suited for home equity financing?</u></b><br>

    •Answer: This approach is best suited for early-stage startups or small businesses where the owner has strong personal assets but limited business credit history. It is often used to fund startup costs, working capital, or early expansion.
</p>


                            

    <p><u><b>5. How much capital can be accessed through home equity?</u></b><br>

    •Answer: The amount depends on the home’s available equity and lender policies. Typically, owners can borrow a portion of their available equity, subject to loan-to-value limits.
</p>


                            

   <p><u><b>6. How quickly can funds be accessed?</u></b><br>

    •Answer: Access timelines vary by lender but are generally faster than traditional business loans. Once approved, funds may be available within weeks, especially through a HELOC.
</p>


                            

 <p><u><b>7. Does using home equity require giving up business equity?</u></b><br>

    •Answer: No. Home equity financing is a non-dilutive funding method. The business owner retains full ownership and control.
</p>
                            

     <p><u><b>8. How is home equity owner debt recorded financially?</u></b><br>

    •Answer: Funds transferred into the business are recorded as an owner loan or shareholder loan (liability). Loan repayments reduce the liability, and interest payments are recorded as expenses.
</p>

                            

   <p><u><b>9. Are interest and repayment required?</u></b><br>

    •Answer: Yes. Home equity loans and HELOCs typically require regular interest payments and principal repayment according to lender terms, regardless of business performance.
</p>

                            

    <p><u><b>10. What happens if the business cannot repay the loan?</u></b><br>

    •Answer: Because the loan is secured by the home, failure to repay can put the owner’s personal residence at risk, including foreclosure. This is the most significant risk of home equity financing.
</p>

                        

   <p><u><b>11. What are the key benefits of using home equity for owner debt?</u></b><br>

    •Answer: Benefits include access to relatively large capital amounts, lower interest rates compared to unsecured loans, non-dilutive funding, and flexibility in how funds are used.
</p>

                        

  <p><u><b>12. What are the risks or limitations of this approach?</u></b><br>

    •Answer: Risks include personal asset exposure, long-term repayment obligations, and increased personal financial stress. It is unsuitable for high-risk or speculative ventures.
</p>

                        

   <p><u><b>13. Can home equity financing be combined with other funding sources?</u></b><br>

    •Answer: Yes. It is commonly combined with grants, accelerators, SBA loans, or personal savings as part of a blended financing strategy.
</p>

                        

 <p><u><b>14. How does home equity financing compare to using cash savings?</u></b><br>

    •Answer: Home equity allows access to larger sums without depleting liquid savings but carries higher personal risk. Cash savings involve lower risk to assets but reduce personal liquidity.
</p>

                        

  <p><u><b>15. How can owners use home equity financing responsibly?</u></b><br>

    •Answer: Owners should borrow conservatively, ensure stable repayment capacity, maintain emergency reserves, and align borrowing decisions with realistic business projections.
</p>    
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def ownerdebthomeequitytwelve(request):
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

    Capital Type: Home Equity</p></center>

 

    <p><b><u>1 - Stage of Development Assessment</b></u><br>

Owner debt funded through home equity is best suited for early-stage to growth-stage businesses that require access to moderate capital but may not yet qualify for traditional business loans. It is often used during startup launch, stabilization, or early expansion phases.
    </p>

   

    <p><b><u>2 - Entity Type Assessment</b></u><br>

This capital source can be applied across all business entity types, including sole proprietorships, partnerships, LLCs, and corporations. Funds are typically injected into the business as an owner loan or capital contribution, depending on accounting and tax treatment.
    </p>

   

    <p><b><u>3 - Pre Capital Assessment</b></u><br>

There are no formal restrictions on prior business funding. Eligibility depends primarily on the owner’s personal creditworthiness and available home equity, rather than the business’s financial history.
    </p>

 

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>

Home equity financing is not market-based and does not involve equity investors. Prior venture capital or business loans do not directly affect eligibility, though lenders may consider overall debt exposure and personal financial risk.
    </p>

 

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>

The amount of capital available depends on the loan-to-value (LTV) ratio of the property and the lender’s policies. This makes it suitable for moderate capital needs, such as working capital, equipment purchases, or early growth initiatives, but not large-scale expansion.
    </p>

   

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Home equity financing does not follow traditional funding rounds. It functions as owner-provided debt, often used as bridge financing or supplemental funding alongside other capital sources.

    </p>

 

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds may be accessed as a single lump sum (home equity loan) or through multiple draws over time (HELOC), providing flexibility based on business cash flow needs.

    </p>

   

    <p><b><u>8 - Use of Funds Assessment</b></u><br>

There are generally no external restrictions on the business use of funds. Common uses include:
<br>•	Startup and operating expenses
<br>•	Inventory and equipment purchases
<br>•	Marketing and sales expansion
<br>•	Short-term cash flow support
However, disciplined financial management is critical since the funding is backed by personal property.

    
</p>

   

    <p><b><u>9 - Risk Assessment</b></u><br>

Risk is high, as the owner’s personal residence is used as collateral. Business failure or cash flow issues may result in personal financial loss or foreclosure, making this one of the riskiest forms of owner debt.
    </p>

 

    <p><b><u>10 - Capital Cost Assessment</b></u><br>

The cost of capital is moderate, typically lower than unsecured loans but higher than some subsidized programs. Interest rates may be variable, and long-term interest costs can accumulate significantly.
    </p>

   

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs may include appraisal fees, legal fees, closing costs, and origination fees. These costs vary by lender and jurisdiction but are generally higher than personal savings or insurance-based loans.

    </p>

 

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>

Timing is moderate, usually ranging from 2–6 weeks, depending on property valuation, credit approval, and legal processing. Faster than many business loans, but slower than personal cash or policy loans.
</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)