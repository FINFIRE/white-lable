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


def commercialbankingrealestateloan(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Commercial Banking</b></u><br>
    Capital Type: Real Estate Loan</center></p>
    
    <p><b><u>Introduction</u></b><br>
    The commercial real estate market in the United States is a major contributor to domestic GDP. According to IBISWorld Industry Research estimates, the commercial real estate market (measured by total revenue) represented USD $1.2 trillion. Commercial real estate is the largest asset class after stocks and bonds (government and investment grade) and is valued at $8.8 trillion in 2021, ahead of cryptocurrencies, art, and others <a href="https://corporatefinanceinstitute.com/resources/commercial-real-estate/commercial-real-estate-lending/">(source)</a>. Commercial business loans help improve cash flow, provide significant funding, and offer long repayment terms while allowing business owners to maintain ownership. They often have low-interest rates and may not require collateral <a href="https://fidelityca.com/advantages-and-disadvantages-of-commercial-business-loans/">(source)</a>.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    1) A real estate loan is used to fund or purchase a property, either private or commercial. A commercial real estate loan is a mortgage secured by a lien on commercial property as opposed to residential property. Commercial real estate (CRE) refers to any income-producing real estate that is used for business purposes. For example, offices, retail, hotels, and apartments. CRE loans are generally made to investors such as corporations or organizations that own and operate commercial real estate. CRE loans are offered by banks, independent lenders, insurance companies, pension funds, private investors, and other capital sources. CRE loans tend to be more expensive than residential loans. CRE loans are sought by small businesses seeking to purchase (acquisition), expand (development), or renovate their sites. CRE loans are generally made to investors such as corporations, developers, partnerships, funds, trusts, and real estate investment trusts (REITs). (Smith, 2021)
    <br>
    <br>2) Commercial real estate loans, often called CRE loans for short, are typically used to purchase, construct, rehabilitate or refinance commercial, industrial and other non-owner-occupied property. That can include office buildings, multi-unit rental buildings, medical facilities, warehouses, hotels or vacant land on which one or more of these types of properties will be built. They can also be used to buy and develop land on which homes will be constructed and sold.
    <br>
    <br>Unlike buying a home with a residential mortgage, the underlying asset for a commercial loan is not a primary residence. Instead, the commercial lender underwrites based on the income — such as rent from tenants — and expenses that the property will generate.
    <br>
    <br>“Ideal candidates to pursue a commercial real estate loan include borrowers who either own the property and are seeking to lower their interest rate by refinancing or seek to obtain capital through a cash-out refinance,” says Chris Moreno, CEO of GoKapital in Miami. “Business owners who rent a location and qualify for a commercial real estate loan may be better off obtaining financing to purchase their business property.” (Martin, 2024)
    <br>
    <br>3) The most common types of CRE loans are:
    <br>&emsp;    • Permanent Loans are first mortgages on a commercial property. A permanent loan must have some amortization and a term of at least five years written into the contract.
    <br>&emsp;    • SBA Loans are written by traditional and non-traditional lenders but are guaranteed by the SBA. There are several different SBA loans that cater to different types of borrowers, the most popular being the 7(a) loan.
    <br>&emsp;    • Bridge Loans provide a short-term first mortgage loan on a commercial property typically with a six-month to a three-year term. Bridge loans are typically obtained when a borrower is waiting for longer-term financing or attempting to refinance an existing obligation.
    <br>(Segal, 2024)
    <br>
    <br>4) Interest rates on commercial loans are generally higher than on residential loans. Also, commercial real estate loans usually involve fees that add to the overall cost of the loan, including appraisal, legal, loan application, loan origination, and/or survey fees.
    <br>
    <br>Another way that commercial and residential loans differ is in the loan-to-value ratio (LTV), a figure that measures the value of a loan against the value of the property. A lender calculates LTV by dividing the amount of the loan by the lesser of the property’s appraised value or its purchase price. (Folger, 2024)
    <br>
    <br>5) Commercial lending is subject to a wide range of regulations at both the state and federal levels. These regulations can impact everything from the types of loans lenders can offer to the fees they can charge. It's important for businesses to work with lenders who are knowledgeable about these regulations and comply with them.
    <br>
    <br>Commercial lending is a complex and highly regulated industry. By understanding the various types of loans, collateral requirements, credit factors, interest rates, and regulatory landscape, businesses can make informed decisions when seeking funding for growth and expansion. (Schable, 2023)
    </p>
                             
    <u><b><p>References</u></b><br>
    Folger, J. (2024, June 10). Commercial Real Estate Loan. Retrieved from Investopedia: <a href="https://www.investopedia.com/articles/personal-finance/100314/commercial-real-estate-loans.asp">https://www.investopedia.com/articles/personal-finance/100314/commercial-real-estate-loans.asp</a>
    <br>Martin, E. J. (2024, May 8). What are commercial real estate or CRE loans? Retrieved from Bankrate: <a href="https://www.bankrate.com/real-estate/commercial-real-estate-loan/">https://www.bankrate.com/real-estate/commercial-real-estate-loan/</a>
    <br>Schable, E. (2023, April 28). 5 Things You May Not Know About Commercial Lending. Retrieved from Farmer's Bank: <a href="https://www.farmerstrust.bank/blog/post/5-things-you-may-not-know-about-commercial-lending">https://www.farmerstrust.bank/blog/post/5-things-you-may-not-know-about-commercial-lending</a>
    <br>Segal, T. (2024, August 31). Commercial Real Estate (CRE) Loan Definition, Types, Terms, Rates. Retrieved from Investopedia: <a href="https://www.investopedia.com/terms/c/commercial-real-estate-loan.asp#">https://www.investopedia.com/terms/c/commercial-real-estate-loan.asp#</a>
    <br>Smith, T. D. (2021). Business Capital 101. San Francisco: Imaginary Press .
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>• Legal Entity Status: The business must be a registered entity (e.g., corporation, LLC, partnership).
    <br>• Clear Ownership and Title: The property must have a clear title, free of legal disputes.
    <br>• Compliance with Zoning and Regulations: The property must comply with local zoning and environmental regulations.
    <br>• Financial Health: The business must provide financial documentation showing it can repay the loan.
    <br>• Legal Authority: The business must have the legal right to enter into the loan agreement and provide necessary governance documents.
    <br>• No Pending Legal Disputes: The business should not be involved in unresolved lawsuits or legal issues.
    <br>• Personal Guarantees: Owners may need to provide personal guarantees to support the loan.
    <br>• Insurance: The business must have appropriate insurance coverage for the property.
    <br>• No Default or Bankruptcy History: The business should not have a history of defaulting on loans or undergoing bankruptcy.
    <br>• AML/KYC Compliance: The business must comply with anti-money laundering and know-your-customer regulations.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Financial Statements: Provide profit and loss, balance sheets, and cash flow statements for the past 2-3 years, along with business and personal tax returns.
    <br>• Business Plan: A detailed plan outlining the company’s operations, growth goals, and projections.
    <br>• Property Documentation: Include property details, an appraisal report, environmental assessments, purchase agreement (if buying), and title report.
    <br>• Legal Documents: Provide articles of incorporation, operating agreements, board resolutions, and personal guarantees from owners or executives.
    <br>• Debt Schedule: A list of all existing debts and liabilities of the business.
    <br>• Insurance Documentation: Proof of property, liability, and business interruption insurance.
    <br>• Lease Agreements: For income-generating properties, provide current lease agreements with tenants.
    <br>• Legal Compliance and Licenses: Ensure the property complies with zoning laws and business licenses, and includes environmental compliance documentation.
    <br>• Background and Credit History: Provide credit reports and any criminal background checks for key stakeholders or business owners.
    <br>• Closing Documents: Include the loan application form, personal financial statements, recent bank statements, and a breakdown of anticipated closing costs.
    </p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def commercialbankingrealestateloanfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Commercial Banking<br>
    Capital Type: Real Estate Loan</center></p>                        
    <p><center><u><b>Frequently Asked Question for Commercial Banking Real Estate Loan</u></b></center></p>
    <p><u><b>1. What is a Commercial Banking Real Estate Loan?</u></b><br>
    • Answer: A Commercial Banking Real Estate Loan is a loan provided by a bank or financial institution specifically for purchasing, refinancing, or improving commercial real estate properties. This type of loan is secured by the property being financed.
    </p>
                             
    <p><u><b>2. What types of real estate can I finance with a Commercial Banking Real Estate Loan?</u></b><br>
    • Answer: You can use the loan for a wide variety of commercial real estate, including office buildings, retail spaces, industrial properties, multi-family residential units, and warehouses. Each lender may have specific property types they specialize in or prefer.
    </p>
                             
    <p><u><b>3. What are the key advantages of using a Commercial Banking Real Estate Loan?</u></b><br>
    • Answer: Some key benefits include lower interest rates (compared to unsecured loans), longer loan terms, and the ability to finance large property acquisitions. Additionally, the loan is secured by the real estate, potentially making it easier to obtain than unsecured financing.
    </p>
                             
    <p><u><b>4. What are the typical loan terms for a Commercial Banking Real Estate Loan?</u></b><br>
    • Answer: Typical loan terms range from 5 to 30 years, depending on the type of property and the lender’s policies. Loan structures may include fixed-rate or variable-rate options, with the interest rate varying based on market conditions.
    </p>
                             
    <p><u><b>5. What is the minimum down payment required for a Commercial Banking Real Estate Loan?</u></b><br>
    • Answer: The down payment typically ranges from 10% to 30% of the property’s purchase price, depending on the type of property, loan type, and the borrower’s financial standing. More favorable terms may be available for businesses with strong credit histories.
    </p>
                             
    <p><u><b>6. What is the interest rate on a Commercial Banking Real Estate Loan?</u></b><br>
    • Answer: Interest rates vary based on factors such as the type of property, loan term, the borrower’s creditworthiness, and market conditions. Typically, the rates range from 3% to 7%, but can fluctuate based on economic conditions.</p>
                             
    <p><u><b>7. How much can I borrow with a Commercial Banking Real Estate Loan?</u></b><br>
    • Answer: The amount you can borrow depends on the value of the property and your business's financial health. Lenders typically offer loans up to 80% to 90% of the property’s appraised value (known as the Loan-to-Value (LTV) ratio).</p>
                             
    <p><u><b>8. How does the bank assess my eligibility for a Commercial Banking Real Estate Loan?</u></b><br>
    • Answer: Lenders will evaluate your credit score, business financials, cash flow, and the value of the property. They will also review your business history, debt-to-income ratio, and the property's potential income (if applicable, for rental properties).</p>
                             
    <p><u><b>9. Are there any prepayment penalties on a Commercial Banking Real Estate Loan?</u></b><br>
    • Answer: Some commercial real estate loans may have prepayment penalties, especially if you pay off the loan early or refinance within a certain time period. However, this depends on the loan agreement and can vary by lender.</p>
                             
    <p><u><b>10. What happens if I default on a Commercial Banking Real Estate Loan?</u></b><br>
    • Answer: If a business defaults, the bank may initiate foreclosure proceedings to recover the outstanding loan balance by taking ownership of the property. It's crucial to communicate with the lender if you're experiencing financial difficulties to avoid foreclosure.</p>
                             
    <p><u><b>11. Can I use a Commercial Banking Real Estate Loan for property renovation or improvement?</u></b><br>
    • Answer: Yes, you can use the loan for renovating, expanding, or improving an existing commercial property. Some lenders offer specialized loans, such as construction loans or renovation loans, specifically for these purposes.</p>
                             
    <p><u><b>12. Can I use a Commercial Banking Real Estate Loan for multiple properties?</u></b><br>
    • Answer: Yes, you can use the loan to finance multiple properties, though the lender may assess each property individually for financing. Portfolio loans may also be available for businesses looking to finance several properties under one loan.
    </p> 
                             
    <p><u><b>13. What are the closing costs associated with a Commercial Banking Real Estate Loan?</u></b><br>
    • Answer: Closing costs typically range from 2% to 5% of the loan amount and may include appraisal fees, title insurance, attorney fees, loan origination fees, and other associated costs.</p>
    
    <p><u><b>14. How long does it take to get approved for a Commercial Banking Real Estate Loan?</u></b><br>
    • Answer: The approval process usually takes 30 to 60 days, depending on the complexity of the loan, the lender’s requirements, and the type of property. The process includes property appraisals, financial review, and underwriting.</p>
    
    <p><u><b>15. Are there any tax benefits associated with a Commercial Banking Real Estate Loan?</u></b><br>
    • Answer: Yes, you may be eligible to deduct the interest payments on the loan as a business expense, which can reduce your taxable income. Additionally, depreciation of the property may also provide tax benefits. It's advisable to consult with a tax professional to understand the specific benefits for your situation.</p>
    
     <p><u><b>16. Can I refinance my Commercial Banking Real Estate Loan in the future?</u></b><br>
    • Answer: Yes, refinancing is often possible if your business’s financial situation improves or if interest rates become more favorable. Refinancing allows you to adjust the loan’s terms, such as the interest rate, payment schedule, or loan amount.</p>
    
     <p><u><b>17. How does the real estate property impact the loan approval process?</u></b><br>
    • Answer: The property’s location, condition, market value, and potential for income generation (if it’s an income-producing property) play a significant role in loan approval. Lenders will typically require an independent property appraisal to determine its current value and viability as collateral.</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def commercialbankingrealestateloantwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR</b></u><br>
    Commercial Banking Real Estate Loan</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    The ideal stage for a company to use a Commercial Banking Real Estate Loan is when the business is established, profitable, and has a defined need for real estate. Companies with strong cash flow, good credit, and collateral will be more likely to secure financing, making this loan type most suitable for businesses that are growing, expanding, or acquiring property to support their ongoing operations.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    The ideal entity types for using a Commercial Banking Real Estate Loan are typically LLCs, corporations (C-Corp or S-Corp), and limited partnerships (LPs or LLPs). These entities provide the liability protection, structural flexibility, and credibility lenders look for when financing commercial real estate transactions. For real estate investment trusts (REITs), this entity type is ideal for large-scale, income-generating properties. Sole proprietorships are less common for real estate loans due to their lack of liability protection, while trusts may be used in specialized cases for estate or inheritance purposes.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    While there are no direct restrictions on how much pre-capital a business has raised before applying for a Commercial Banking Real Estate Loan, but the amount and type of pre-capital can impact the loan process. Businesses with significant pre-capital, especially equity, may be viewed favorably as they are seen as financially stable and capable of handling debt obligations. However, businesses with excessive debt or high-risk capital may face scrutiny regarding their ability to manage additional borrowing.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    While there are no direct restrictions based on how much pre-capital a company has raised, certain types of pre-capital raising, particularly if they involve high levels of debt, complex ownership structures, or non-operational uses of funds, could create challenges when applying for a Commercial Banking Real Estate Loan. Lenders focus on the financial stability, debt management, and ownership structure of a business when assessing eligibility for a real estate loan, so businesses that have raised pre-capital in ways that increase financial risk or complicate the decision-making process could face obstacles.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    A company can raise anywhere from 65% to 80% of the value of the real estate being financed through a Commercial Banking Real Estate Loan, subject to factors like the loan-to-value (LTV) ratio, property type, income potential, and the company’s financial health. This means that, for example, a company purchasing a $1 million property could borrow between $650,000 and $800,000 depending on the lender’s policies and the company’s financial situation. However, the final loan amount will depend on the property's appraisal, the company’s debt service coverage, and the specific terms and conditions of the loan.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    The ideal capital round for securing a Commercial Banking Real Estate Loan is typically at the Series B or later stage, once a company has achieved a certain level of stability, revenue generation, and financial credibility. At these stages, companies are more likely to have the necessary equity, strong cash flow, and the ability to meet loan repayment obligations, making them attractive candidates for real estate financing. However, companies in earlier rounds (e.g., Series A) can still be eligible if they have a solid financial foundation and a viable business plan.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    When raising capital using a Commercial Banking Real Estate Loan, the number of tranches is typically one, meaning the loan is usually provided as a single lump sum.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    A business can use the funds from a Commercial Banking Real Estate Loan for various real estate purposes, including purchasing property, making property improvements, funding construction, or refinancing existing real estate loans. However, there are strict restrictions on how the funds can be used. They must be tied to real estate activities and cannot be used for unrelated business expenses.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Businesses should have moderate risk tolerance if they are looking to use a commercial real estate loan, as they need to be ready to navigate potential market fluctuations, manage the long-term debt, and handle any unexpected property-related issues. The business must be able to generate consistent revenue from the property to comfortably meet loan obligations.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    A business seeking a Commercial Banking Real Estate Loan should have a moderate to high level of capital cost tolerance. This means the business must be financially prepared for significant initial costs (down payments, closing fees, and legal expenses), as well as ongoing costs (loan interest, property maintenance, and possible renovations). The business should also be comfortable with the risk of potentially higher interest rates and the long-term nature of the loan, which may result in a large financial commitment.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    For a $1 million commercial real estate loan, a business can expect to pay $220,000 to $235,000 or more in upfront costs, depending on the down payment, fees, and property requirements. These upfront costs include the down payment, loan origination fees, legal and title costs, appraisals, inspections, and any other expenses associated with securing the loan and purchasing the property.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    A company can typically expect to receive capital from a Commercial Banking Real Estate Loan within 30 to 60 days. The timeline depends on the efficiency of the business in submitting required documents, the lender’s processes, and the complexity of the property being financed.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)