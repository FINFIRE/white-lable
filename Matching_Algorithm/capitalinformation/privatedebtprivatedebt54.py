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


def privatedebtprivatedebt(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Debt</b></u><br>
    Capital Type: Private Debt</center></p>
    
    <p><b><u>Introduction</u></b><br>
    Wondering why a company might choose to finance with debt? In a few words: It’s considered more cost-efficient. More specifically, the interest payments that a borrower owes a lender typically has a fixed timeframe and will conclude when the debt matures, while equity holders have ownership of a company’s owners in perpetuity. Also, interest expenses can be used as tax-write-offs <a href="https://pitchbook.com/blog/what-is-private-debt">(source)</a>.
    <br>According to Preqin, the estimated assets under management (AUM) globally in 2023 reached nearly $1.7 trillion in the private debt market <a href="https://www.stepstonegroup.com/news-insights/corporate-private-debt-primer">(source)</a>.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    1) Private debt includes any debt held by or extended to privately held companies. It comes in many forms, but most commonly involves non-bank institutions making loans to private companies or buying those loans on the secondary market. A variety of investors, or private debt funds, are involved in this space. This is grouped into the following subgroups: 1) acquisition loans; 2) asset-based lending; 3) bridge financing; 4) collateralized debt obligation (CDO)-“is a complex structured finance product that is backed by a pool of loans and other assets and sold to institutional investors. A CDO is a particular type of derivative because, as its name implies, its value is derived from another underlying asset. These assets become the collateral if the loan defaults”; 5) private loans; 6) hard money loans- “are a type of loan that is secured by real property. Hard money loans are considered loans of "last resort" or short-term bridge loans. These loans are primarily used in real estate transactions, with the lender generally being individuals or companies and not banks”; 7) promissory notes; or 8) real estate loans. (Smith, 2021) 

    <br><br>Private debt is a form of debt financing offered by non-bank lenders—including, for instance, large GPs already active in the private equity market—that is not issued or traded by traditional public markets. Small and midsize companies often turn to private lenders because they either cannot or choose not to use public markets for debt financing and choose not to obtain financing from banks. Depending on the sub-strategy within private debt, the debt will sit at a different position in the company’s capital structure but will remain above common equity.

    <br><br>For borrowers, it provides flexible terms and customized financial solutions as well as higher certainty of execution, typically in a tighter time frame if needed. Moreover, thanks to the private nature of the asset class, firms do not have to disclose their books to the public/competitors.

    <br><br>Because private debt investments are illiquid credit investments, investors should understand two types of risks when allocating capital to the asset class: liquidity and credit risks.

    <br><br>From an investor’s perspective, private debt provides higher risk-adjusted returns at lower volatility compared with public debt. Over the past few years, the private debt landscape has broadened to offer various sub-strategies and implementation options, each with different risk and return profiles. As a result, the investor base in private debt is diverse, including institutions like pension funds and insurance companies, as well as private individuals and investment funds. (Corporate private debt primer, 2024)

    <br><br>3) Private debt vs private equity: 
    Debt and equity are two broad categories that make up the capital markets, and both are important components of financing companies—both public and private. A company’s capital structure will contain a mix of equity and debt to finance their operations.

    <br><br>With private debt financing, ownership is retained by the company. However, they must sign a contract with the debt investor (or lender). As the borrower, the company is legally required to pay the lender. There’s no such guarantee of a return for equity investors. Because debt investors are more senior investors in the capital stack, they get paid out first in a workout. For these reasons, debt investing is typically seen as lower risk, lower return, and more stable from a cash flow perspective than equity investing.

    <br><br>In equity financing, the investor receives partial ownership in the company they are providing financing to, and therefore, a claim to all future earnings. These claims are rewarded as dividends paid out to the equity investor or stockholder. Equity investing is lower in priority in case of a liquidation event, and it has the highest risk and highest cost.

    <br><br>Private credit vs private debt:
    <br>You will sometimes see private debt and private credit used interchangeably. However, an important distinction is that private credit is just one type of private debt.

    <br><br>Private credit, or direct lending, is defined as directly originated loans to corporate borrowers that are not broadly syndicated. They are typically unrated, and borrowers tend to be small to midsized companies. However, in recent years, larger borrowers have issued this type of financing as well.

    <br><br>Private credit is typically provided by a non-bank lender, or a small group of lenders in a club deal. That said, there are some cases where a bank is one of the lenders alongside an alternative lender or lenders. As mentioned above, this often includes general partners. (Martinez, 2024)
    </p>
                             
    <u><b><p>References</u></b><br>
    Corporate private debt primer. (2024, April 9). Retrieved from Stepstone Group: <a href="https://www.stepstonegroup.com/news-insights/corporate-private-debt-primer">https://www.stepstonegroup.com/news-insights/corporate-private-debt-primer</a>
    <br><br>Martinez, K. K. (2024, February 9). What is private debt? The ultimate guide (2024). Retrieved from Pitchbook: <a href="https://pitchbook.com/blog/what-is-private-debt">https://pitchbook.com/blog/what-is-private-debt</a>
    <br><br>Smith, T. D. (2021). Business Capital 101. San Francisco: Imaginary Press.
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>• Business Structure: Must be a legally recognized entity (corporation, LLC, etc.).
    <br>• Operational History: Typically at least 6 months to 1 year of operations.
    <br>• Creditworthiness: Satisfactory credit history or ability to repay the loan.
    <br>• Collateral: Must have assets to pledge (e.g., real estate, inventory) for secured debt.
    <br>• Regulatory Compliance: Must comply with all local, state, and federal regulations.
    <br>• No Active Bankruptcy: The business should not be in bankruptcy or facing major legal disputes.
    <br>• Financial Health: Meet debt-to-equity ratio requirements or demonstrate profitability and cash flow.
    <br>• Clear Use of Funds: Must have a defined purpose for the capital (e.g., expansion, acquisition).
    <br>• Documentation: Provide accurate financial statements and legal documents (e.g., tax returns).
    <br>• Management Team: Experienced management team with a track record of financial stability.
    <br>• Non-Compete/Restrictions: Avoid conflicts of interest or operational restrictions.
    <br>• No Tax Liens/Judgments: Must not have unresolved tax liens or legal judgments.
    </p>
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Financial Statements (Balance Sheet, Income Statement, Cash Flow Statement)
    <br>• Tax Returns (Business & Personal, typically for the last 2-3 years)
    <br>• Business Plan or Loan Proposal
    <br>• Collateral Documentation (Appraisals, Ownership Documents)
    <br>• Debt Schedule (Existing debts and liabilities)
    <br>• Legal Entity Documentation (Articles of Incorporation, Operating Agreement, EIN)
    <br>• Personal Guarantee (if applicable, including Personal Financial Statement)
    <br>• Credit Reports (Business and Personal)
    <br>• Cash Flow Projections (Next 12–24 months)
    <br>• Legal Documents (Licenses, Contracts, Agreements)
    <br>• Management Information (Team bios, Ownership structure)
    <br>• Insurance Documents (Proof of business insurance)
    <br>• Market & Competitive Analysis
    <br>• Existing Loan Agreements (If applicable)
    <br>• Repayment Strategy/Debt Service Plan
    </p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privatedebtprivatedebtfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Private Debt<br>
    Capital Type: Private Debt</center></p>                        
    <p><center><u><b>Frequently Asked Question for Bridge Financing</u></b></center></p>
    <p><u><b>1. What is Private Debt, and how does it differ from traditional bank loans?</u></b><br>
    • Answer: Private Debt refers to non-publicly traded debt raised from private sources like private equity firms, hedge funds, and specialized lenders. Unlike traditional bank loans, private debt often provides more flexible terms and faster access to capital.</p>
                             
    <p><u><b>2. What types of Private Debt options are available to businesses?</u></b><br>
    • Answer: The key types of Private Debt include:
    <br>- Acquisition Loans: Loans used to finance the purchase of another company.
    <br>- Asset-Based Lending (ABL): Loans secured by business assets like receivables or inventory.
    <br>- Bridge Financing: Short-term loans to cover immediate funding needs until long-term financing is secured.
    <br>- Collateralized Debt: Loans secured by the borrower’s collateral, typically physical assets.
    <br>- Hard Money Loans: Loans secured by real estate, often used for projects requiring quick financing.
    <br>- Promissory Notes: Unsecured or secured short-term debt instruments where the borrower agrees to repay the loan by a specific date.
    <br>- Real Estate Loans: Loans used specifically for acquiring, refinancing, or developing real estate.</p>
                             
    <p><u><b>3. Why should I consider Private Debt for my business rather than other financing options?</u></b><br>
    • Answer: Private debt is often ideal for companies that require more flexible terms than traditional bank loans, especially if they have unique financing needs, a short timeline, or assets to pledge as collateral. It can also be more accessible if the company has a higher risk profile.</p>
                             
    <p><u><b>4. What are the benefits of using an Acquisition Loan?</u></b><br>
    • Answer: Acquisition loans can help you finance the purchase of another business with more favorable terms than equity financing. This allows you to preserve your equity stake while benefiting from the target company's future profits.</p>
                             
    <p><u><b>5. How does Asset-Based Lending (ABL) work, and is it right for my company?</u></b><br>
    • Answer: ABL involves borrowing against your business assets like receivables, inventory, or equipment. It’s an excellent option for businesses with significant assets but limited cash flow. The amount you can borrow is determined by the value of these assets.</p>
                             
    <p><u><b>6. What is Bridge Financing, and when should my business use it?</u></b><br>
    • Answer: Bridge financing provides short-term capital to "bridge" the gap until more permanent financing is secured. It’s useful if you need quick access to funds, such as during the interim period between a major deal or refinancing.</p>
                             
    <p><u><b>7. How do Collateralized Debt and Hard Money Loans differ from each other?</u></b><br>
    • Answer: 
    <br>- Collateralized Debt is backed by assets like property or inventory but can be structured more flexibly across various types of collateral.
    <br>- Hard Money Loans are typically short-term loans secured by real estate and used for quick, high-risk financing, such as property renovations or flipping.</p>
                             
    <p><u><b>8. What are the risks associated with using Private Debt?</u></b><br>
    • Answer: The primary risks include higher interest rates compared to traditional loans, the possibility of asset forfeiture if the debt is secured, and the pressure to repay within a   short timeframe (especially for bridge loans or hard money loans).</p>
                             
    <p><u><b>9. What types of businesses typically use Private Debt?</u></b><br>
    • Answer: Private debt is often used by middle-market businesses, startups, real estate investors, or companies with a specific, time-sensitive capital need. It is also common for companies in distress or those with lower credit ratings who may not qualify for traditional financing.</p>
                             
    <p><u><b>10. What kind of terms can I expect with Private Debt?</u></b><br>
    • Answer: Terms vary depending on the type of loan and lender but may include:
    <br>- Short-term to medium-term repayment (ranging from a few months to several years).
    <br>- Higher interest rates due to the higher risk involved.
    <br>- Specific covenants or collateral requirements.
    <br>- Flexible repayment schedules compared to traditional financing.</p>
                             
    <p><u><b>11. How do interest rates for Private Debt compare to traditional bank loans?</u></b><br>
    • Answer: Private debt typically comes with higher interest rates due to the higher risk taken by lenders. However, the flexibility and speed of access to capital can justify the cost for businesses with urgent or unconventional financing needs.</p>
                             
    <p><u><b>12. Can my business qualify for Private Debt if we don’t have substantial assets or collateral?</u></b><br>
    • Answer: While many forms of private debt require assets as collateral, there are options like Promissory Notes or unsecured Bridge Financing that may not require significant collateral. Your business's financial health, cash flow, and future projections may still play a significant role in approval.</p> 
                             
    <p><u><b>13. How long does it take to secure Private Debt financing?</u></b><br>
    • Answer: Private debt can typically be arranged much faster than traditional bank financing—sometimes within a few weeks or even days—due to fewer regulatory hurdles and more flexible underwriting processes.</p>

    <p><u><b>14. What are the potential downsides of using Private Debt?</u></b><br>
    • Answer: The main downsides include higher costs (due to interest rates and fees), the risk of losing pledged assets, and the pressure of having to repay in a relatively short period, which can affect cash flow and long-term stability.</p>
    
    <p><u><b>15. How is Private Debt structured?</u></b><br>
    • Answer: Private debt structures can vary widely. Some may involve fixed or floating interest rates, secured or unsecured loans, and different repayment schedules. Some lenders may also include performance-based covenants, such as maintaining certain financial ratios.</p>
    
    <p><u><b>16. What happens if my business defaults on Private Debt?</u></b><br>
    • Answer: If you default on a private debt, the lender may seize the collateral securing the loan (in the case of asset-based lending, hard money loans, or collateralized debt) or pursue legal action to recover the funds.</p>
    
    <p><u><b>17. Are there any tax implications associated with using Private Debt?</u></b><br>
    • Answer: Interest payments on private debt are generally tax-deductible, similar to other types of business loans. However, the specific tax treatment depends on your jurisdiction and the structure of the loan, so it's advisable to consult with a tax professional.</p>
    
    <p><u><b>18. Can Private Debt be used for business expansion or only for acquisitions?</u></b><br>
    • Answer: Yes, private debt can be used for business expansion, working capital, or general corporate purposes, not just acquisitions. Asset-based lending, bridge financing, and other forms of private debt can help fund growth projects, new product lines, or operational needs.</p>
    
    <p><u><b>19. What are Promissory Notes, and how do they work in Private Debt?</u></b><br>
    • Answer: A promissory note is a simple debt instrument where your business promises to repay a specific amount within a set time frame. This can be a flexible option when you need funding quickly and don’t want the complexity of formalized loans.</p>
    
    <p><u><b>20. How can my business assess whether Private Debt is the best option compared to equity financing or venture capital?</u></b><br>
    • Answer: Private debt is often more attractive than equity financing because it allows you to maintain full control of your business. However, it may come with higher short-term costs and repayment pressures. Equity financing, on the other hand, may dilute ownership but offers more flexibility regarding repayment. Your decision should be based on the capital needs, repayment capacity, and long-term goals of your business.</p>                         
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privatedebtprivatedebttwelve(request):
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
    Private Debt</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    Startups or early-stage companies may also use Promissory Notes or Bridge Financing in certain scenarios. Since private debt usually requires some form of collateral or proven cash flow, startups may only be able to access certain types of private debt, such as Promissory Notes.

    <br><br>Asset-Based Lending (ABL), Collateralized Debt, and Real Estate Loans are often ideal for mid-stage companies that have significant assets, steady cash flow, and a proven track record. Bridge Financing is also relevant for businesses in this stage that require short-term capital.
    
    <br><br>Businesses that are more mature, with stable revenue and assets, are prime candidates for Acquisition Loans to acquire other companies or assets. Hard Money Loans or Real Estate Loans might also be appropriate if the business is involved in real estate investments or development projects and requires quick capital.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    While private debt can be used by a variety of entity types, the most ideal are LLCs and Corporations (C-Corps) due to their asset protection, scalability, and ability to leverage assets for financing. Partnerships and sole proprietorships may also use private debt, but they face more challenges in terms of liability and collateral.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    There are no restrictions preventing businesses that have raised pre-capital (equity or other forms of funding) from using private debt. However, there may be some considerations around the terms and structure of the pre-capital and how they impact the company’s financial profile and borrowing capacity.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    The way in which a company has raised pre-capital can create restrictions when using private debt. The key areas of concern include:
    <br>• Covenants in prior equity or debt agreements that limit the ability to take on additional debt.
    <br>• Debt-to-equity ratio limits or subordination clauses that affect the company’s borrowing capacity.
    <br>• Investor rights (such as liquidation preferences or control rights) that could interfere with the company’s ability to secure new debt financing.
    <br>• Collateral issues where existing secured debt limits the use of assets for future debt.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    The amount a company can raise using private debt depends largely on its collateral value, cash flow, financial health, and the type of debt instrument used. Companies with solid assets and strong financials can raise significant amounts, ranging up to several hundred million dollars. Smaller or higher-risk businesses may be limited to smaller loans in the $500,000 to $10 million range.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Private debt is least risky for companies that are in the growth and expansion stages, typically after they have secured Series A, B, or later rounds.
    <br>-Growth Stage: Ideal for Acquisition Loans, Asset-Based Lending, Bridge Financing, and Real Estate Loans.
    <br>-Expansion Stage: Often relies on Bridge Financing, Asset-Based Lending, and Real Estate Loans.
    <br>-Mature Stage: Larger companies can access Promissory Notes, Acquisition Loans, and Collateralized Debt.
    <br>-For early-stage companies in the seed or pre-revenue stages, private debt is typically not a viable option, and the focus should be on equity financing or other alternatives that do not require repayment obligations.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Ultimately, the number of tranches should reflect the company’s specific financing needs, growth stage, and the lender's appetite for risk, as well as the terms that are most favorable to both the company and the lender.
    <br>Single Tranche: Best for smaller or more straightforward loans with clear capital needs and repayment terms.
    <br>Two Tranches: Suitable for companies that need an initial infusion of capital with the flexibility to raise more once certain milestones or conditions are met.
    <br>Three or More Tranches: Ideal for larger, more complex capital raises, where funding is tied to specific phases, milestones, or projects. This structure works well for growth-stage companies, acquisitions, or expansion projects that require phased financing.</p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    In general, there are no restrictions for how a business can use funds from private debt. A business can use funds from private debt in a variety of ways depending on the specific debt product and the company’s needs. The flexibility of private debt allows companies to address short-term and long-term financial challenges, support growth, fund acquisitions, and manage operational costs.</p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    A business using private debt should generally have a moderate to high risk tolerance, as it involves assuming significant financial obligations that must be met on time. This is especially true for companies using debt instruments that are secured by collateral or those with stringent repayment schedules, such as Hard Money Loans, Promissory Notes, or Acquisition Loans.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    A business should have a moderate to high capital cost tolerance if it intends to use private debt, as the capital costs associated with these types of financing are generally higher than traditional debt sources. The company must be able to absorb higher interest rates, origination and transaction fees, shorter repayment periods and collateral risks.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    On average, a company may spend 2% to 10% of the total loan amount on upfront costs when raising private debt, with these costs typically including origination fees, due diligence costs, legal fees, appraisal fees, and other transaction-related expenses. The specific amount depends on factors such as loan size, collateral complexity, and the financial condition of the borrowing company.</p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    In general, businesses can expect to receive capital from private debt in 2 to 8 weeks, with the speed depending on the type of loan, the complexity of the deal, and the efficiency of the lender's process. For time-sensitive situations, options like Hard Money Loans or Bridge Financing are the quickest.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)