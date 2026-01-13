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


def smallbusinessadministrationsbic(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Small Business Administration</b></u><br>
    Capital Type: SBIC</center></p>
    
    <p><b><u>Introduction</u></b><br>
    As of June 30, 2023, there were 312 licensed SBICs with approximately $23.34 billion of private capital and $113.451 billion of outstanding SBA leverage (of which $13.427 billion is debenture leverage and $24 million is other SBA leverage) <a href=" https://www.troutman.com/insights/description-of-the-small-business-investment-company-debenture-program-october-2023.html">(source)</a>.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    1) An SBIC is a privately owned company that’s licensed and regulated by the SBA. SBICs invest in small businesses in the form of debt and equity. The SBA doesn’t invest directly into small businesses, but it does provide funding to qualified SBICs with expertise in certain sectors or industries. Those SBICs then use their private funds, along with SBA-guaranteed funding, to invest in small businesses.

    <br><br>SBICs invest in small businesses through debt, equity, or a combination of both. A typical SBIC investment is made over a 3-year period. (Investment capital, 2024)

    <br><br>2) SBIC’s offer venture capital financing to higher-risk small businesses, and SBIC loans are guaranteed by the SBA. SBICs use a combination of funds raised from private sources and money raised through the use of SBA guarantees to make equity and mezzanine capital investments in small businesses. 

    <br><br>3) SBICs must invest only in “small businesses”, defined as companies with net worths of $19.5 million or less and average net income after-taxes of $6.5 million or less for the prior two fiscal years. SBICs must invest at least 25 percent of financings in “smaller enterprises” that have a tangible net worth of less than $6 million and average net income after-taxes for the prior two years no greater than $2 million. Even if a company does not meet these tests, it still may qualify as a small business and smaller enterprise depending on the company’s industry group and the number of its employees or size of annual revenues.
    </p>
                             
    <u><b><p>References</u></b><br>
    
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>Businesses seeking SBA SBIC loans or investments must be small, for-profit entities with U.S. ownership and meet SBA size standards.
    <br>They must use the funds for expansion or operational purposes and not for passive investments.
    <br>The business must work with a licensed SBIC firm, which will provide the funding under SBA regulations.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br> 1. Business Plan
    <br> A comprehensive business plan is crucial for the application process. This should include:
    <br> Business overview: Company mission, history, and goals.
    <br> Market analysis: Information on the industry, target market, competition, and market trends.
    <br> Financial projections: Expected income, profit margins, cash flow projections, and break-even analysis.
    <br> Use of funds: A clear explanation of how the funds will be used to grow the business (e.g., expansion, working capital, equipment purchase, etc.).
    <br> Management team: Background and experience of the company’s management team and key personnel.
    <br> 2. Financial Statements
    <br> Historical financial statements: Typically, SBICs will require financial statements for the last three years (if applicable). These include:
    <br> Balance sheets
    <br> Income statements (Profit & Loss statements)
    <br> Cash flow statements
    <br> Interim financial statements: In addition to historical statements, you may also need to provide up-to-date, interim financial statements that reflect the most recent period (quarterly or monthly).
    <br> Tax returns: The last three years of federal tax returns for the business, which help to verify the company's financial history and tax obligations.
    <br> 3. Personal Financial Statements
    <br> Personal financial statements of key business owners or executives (particularly those with significant ownership stakes, often 20% or more) are usually required. This document provides a snapshot of the individual's assets, liabilities, and net worth.
    <br> This may include:
    <br> Personal assets (real estate, vehicles, investments, etc.)
    <br> Personal liabilities (mortgages, loans, credit obligations, etc.)
    <br> Income and employment details
    <br> 4. Loan History and Debt Schedule
    <br> A detailed list of all current debts and obligations of the business, including any outstanding loans, lines of credit, or other financial liabilities. This is used to evaluate the company’s existing debt load and its ability to handle additional financing.
    <br> Include terms of each debt (interest rate, maturity date, payment schedule) and the current status of repayment.
    <br> 5. Ownership and Legal Structure Documents
    <br> Business entity documents: Proof of the legal structure of the business (e.g., corporation, LLC, partnership). These may include:
    <br> Articles of Incorporation or Operating Agreement
    <br> Partnership Agreements, if applicable
    <br> Bylaws (for corporations)
    <br> Ownership structure: A breakdown of the ownership percentages, including names and addresses of shareholders or members with more than 20% ownership.
    <br> List of board members (if applicable).
    <br> 6. Licenses, Permits, and Registrations
    <br> Copies of any business licenses and permits required for the business to operate legally in its industry or state.
    <br> State and federal registrations that demonstrate compliance with regulatory requirements (e.g., state incorporation certificates, federal employer identification number (EIN), etc.).
    <br> 7. Valuation Documents
    <br> If the loan or investment involves equity or a convertible debt structure, the business may need to provide a business valuation or valuation report that establishes the company’s worth. This is often conducted by a third-party valuation expert.
    <br> 8. Use of Proceeds
    <br> A detailed breakdown of how the loan or investment funds will be used. For example, if the business is seeking capital for expansion, the documentation should show:
    <br> Equipment purchases
    <br> Real estate investment
    <br> Hiring new employees or launching new marketing campaigns
    <br> Working capital for inventory or operational costs
    <br> 9. Management Resumes and Background Information
    <br> Resumes or bios for the key members of the management team. This will demonstrate the experience and expertise of the leadership team and help the SBIC assess whether they can successfully implement the business plan and grow the company.
    <br> Personal history statements may also be required to assess the background and qualifications of business owners or executives.
    <br> 10. Legal Documents
    <br> Legal disputes: If applicable, any documents related to current or past legal disputes, lawsuits, or claims involving the business. This includes pending litigation, judgments, or any other legal concerns that may affect the business.
    <br> Contracts and agreements: Any significant contracts or agreements (e.g., supplier contracts, partnership agreements, leases, intellectual property agreements, etc.) that may impact the business’s operations.
    <br> 11. Market and Industry Information
    <br> Market research reports: Documents that support the business’s understanding of its market and industry, including demand trends, target demographics, competitive landscape, and other factors that support its growth potential.
    <br> Customer and supplier lists: Information about the company's key customers, contracts, and supplier relationships that help demonstrate the business’s position in its industry.
    <br> 12. Environmental and Regulatory Compliance (if applicable)
    <br> If the business operates in an industry with regulatory or environmental requirements (e.g., manufacturing, construction, healthcare), it may need to provide proof of compliance with local, state, and federal regulations.
    </p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def smallbusinessadministrationsbicfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Small Business Administration<br>
    Capital Type: SBIC</center></p>                        
    <p><center><u><b>Frequently Asked Question for SBIC</u></b></center></p>
    <p><u><b>1. What is an SBA SBIC?</u></b><br>
    • Answer: The SBA SBIC program enables licensed private investment firms to provide funding to small businesses in the form of debt or equity investments. The U.S. Small Business Administration (SBA) partners with these firms to offer businesses access to growth capital with favorable terms.</p>
                             
    <p><u><b>2. How is SBA SBIC funding different from other funding options?</u></b><br>
    • Answer: Unlike traditional loans or venture capital, SBA SBIC funding is backed by the government, offering potentially more favorable loan terms and access to funding that might otherwise be unavailable through commercial lenders or investors. It can also provide equity investments without requiring immediate repayment.</p>
                             
    <p><u><b>3. What types of businesses are eligible for SBA SBIC funding?</u></b><br>
    • Answer: SBA SBIC funding is available to small businesses that meet the SBA’s size standards and are involved in for-profit activities. These businesses generally need to be growing, have a solid management team, and demonstrate a potential for strong financial returns. The business should also typically need capital to expand, develop, or restructure.</p>
                             
    <p><u><b>4. Is my business eligible if it has already raised capital or is in a growth stage?</u></b><br>
    • Answer: Yes, you can still apply for SBA SBIC funding if you have already raised capital or are in a growth phase. In fact, SBA SBICs often target businesses that are in the expansion or mature growth stages, especially those seeking growth capital to scale their operations.</p>
                             
    <p><u><b>5. Are there any industry restrictions on the businesses that can use SBA SBIC funding?</u></b><br>
    • Answer: SBA SBIC funding is generally available to most industries, but certain businesses may be excluded, such as those involved in real estate, gambling, lending (like payday loans), or other speculative ventures. SBICs typically prefer investing in businesses that show long-term growth potential.
    </p>
                             
    <p><u><b>6. What types of financing do SBA SBICs offer?</u></b><br>
    • Answer: SBA SBICs can provide equity financing, mezzanine financing, and debt financing. The exact structure of the financing depends on the needs of the business and the terms negotiated with the investor. Debt financing typically involves long-term loans, while equity financing involves selling ownership stakes to investors.</p>
                             
    <p><u><b>7. How much funding can a business raise through an SBA SBIC?</u></b><br>
    • Answer: The amount a business can raise varies, but generally, SBA SBICs provide equity investments ranging from $1 million to $15 million or more. Debt investments typically range from $500,000 to $10 million depending on the business’s needs and qualifications.</p>
                             
    <p><u><b>8. Do SBA SBICs provide both equity and debt financing?</u></b><br>
    • Answer: Yes, SBA SBICs can provide both equity and debt financing, depending on the company’s needs and the terms of the deal. Equity investments typically involve giving up a share of ownership, while debt financing requires repayment over time, usually with interest.</p>
                             
    <p><u><b>9. How long does it take to receive funding from an SBA SBIC?</u></b><br>
    • Answer: The timeline can vary but typically takes 3 to 6 months from the initial application to the disbursement of funds. The process involves due diligence, negotiation, and obtaining necessary regulatory approvals. Businesses should be prepared for a comprehensive review process.</p>
                             
    <p><u><b>10. What are the key steps in applying for SBA SBIC funding?</u></b><br>
    • Answer: The main steps include: 
    <br>- Initial inquiry and preparation of documents (business plan, financials, projections).
    <br>- Due diligence by the SBA SBIC, reviewing financials, operations, and management.
    <br>- Negotiation of terms (interest rates, equity share, repayment schedules).
    <br>- Approval and finalization of the investment agreement.
    <br>- Funding disbursement once all paperwork and compliance checks are completed.</p>
                             
    <p><u><b>11. What are the costs associated with SBA SBIC funding?</u></b><br>
    • Answer: While SBA SBIC funding offers competitive terms, businesses should expect upfront costs such as legal fees, financial advisory fees, and potential due diligence costs. These could range from $20,000 to $100,000 or more depending on the size of the deal. Additionally, there may be transaction fees (typically 1%–5% of the financing amount) and other associated costs.</p>
                             
    <p><u><b>12. What are the typical terms for SBA SBIC debt financing?</u></b><br>
    • Answer: SBA SBIC debt financing typically comes with lower interest rates than traditional bank loans, but repayment terms can vary. These loans often have longer terms (5 to 10 years) with flexible repayment schedules, and they may include interest-only periods in the early years to help businesses manage cash flow.
    </p> 
                             
    <p><u><b>13. What is the ownership structure like for equity financing from an SBA SBIC?</u></b><br>
    • Answer: If the SBA SBIC provides equity financing, the business will need to give up a portion of ownership. The percentage of ownership given to the investor depends on the size of the investment and the valuation of the business. Typically, SBICs may seek 20-40% equity in exchange for substantial capital, but this can vary.</p>

    <p><u><b>14. What are the risks associated with SBA SBIC funding?</u></b><br>
    • Answer: The main risks include ownership dilution (if taking equity financing), debt obligations (if taking debt financing), and potential pressure for an exit strategy (such as a sale or IPO). Businesses should also consider the control they may have to share with investors and the commitment required for debt repayment.</p>
    
     <p><u><b>15. Can I apply for SBA SBIC funding if my business is not profitable yet?</u></b><br>
    • Answer: It is possible, but the business must demonstrate a clear growth path, strong management, and future profitability potential. Many SBA SBICs are open to high-growth businesses that may not yet be profitable but have a solid business plan and a potential for strong returns.</p>
    
    <p><u><b>16. Why should I choose SBA SBIC funding over venture capital or traditional bank loans?</u></b><br>
    • Answer: SBA SBIC funding can be a great option for businesses that want flexible terms, lower interest rates (in the case of debt), or equity capital without immediate repayment obligations. SBICs also provide access to valuable expertise, mentorship, and networks that can help businesses grow. Additionally, the government backing often results in better terms than traditional commercial lenders or venture capitalists.</p>
    
    <p><u><b>17. What are the main advantages of SBA SBIC funding?</u></b><br>
    • Answer:     
    <br>- Lower interest rates compared to traditional loans.
    <br>- Flexible terms and a variety of financing options (equity, debt, or a mix).
    <br>- Government-backed support, which can make it easier to access capital.
    <br>- Expertise and potential mentorship from experienced investors.
    <br>- No immediate repayment pressure if financing is equity-based.
    </p>
    
    <p><u><b>18. Why should I choose SBA SBIC funding over venture capital or traditional bank loans?</u></b><br>
    • Answer: 
    <br>- Ownership dilution (if taking equity financing).
    <br>- Longer approval and funding timelines compared to traditional lenders.
    <br>- The potential complexity of negotiations and terms.
    <br>- Not suitable for businesses looking for very small, quick loans.</p>             
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def smallbusinessadministrationsbictwelve(request):
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
    Capital Type: SBA SBIC</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    The ideal stage of development for a company seeking SBA SBIC funding is typically the growth or expansion stage, where the company has proven its business model, is generating stable revenue, and is looking for significant capital to scale operations or expand into new markets. SBICs are designed to provide capital to businesses that are established, have a solid foundation, and are poised for rapid growth.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    The ideal entity type for a business seeking SBA SBIC funding is generally a corporation (especially a C-Corp) or a limited liability company (LLC), especially if they are structured to allow equity investments. These entity types provide the flexibility and structure that SBICs prefer for making equity or debt investments in growing businesses. LLCs and corporations align well with the investment models used by SBICs and offer the necessary ownership and governance flexibility.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    Businesses that have already raised pre-capital can still apply for SBA SBIC funding, and in many cases, it can work to their advantage. Pre-capital indicates that the business has reached a stage of maturity and is ready for additional funding to drive growth and expansion. The important thing is to ensure that the business is in a position to use the capital effectively and that any previous capital raises are not overly complicated or conflicting with SBIC terms.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    While having raised pre-capital is generally acceptable and can actually make a business more attractive to an SBA SBIC, the terms and structure of that pre-capital can present challenges. Companies need to be mindful of the following potential issues:
    <br>• Excessive debt or complex debt structures
    <br>• Unfavorable equity terms, such as heavy dilution or investor control
    <br>• Conflicting or complex investment terms
    <br>• Ownership conflicts
    <br>• Previous investors who may not meet SBA requirements
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    The amount a company can raise using SBA SBIC services varies depending on several factors, including the size of the SBIC, the business’s needs, and the type of financing (equity or debt). Businesses can expect to raise up to $10 million through SBIC funding, but larger investments may be possible depending on the specific circumstances.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    The ideal capital round for a business seeking SBA SBIC funding is usually a Series A or Series B round when the company is in the growth or expansion phase. At this stage, businesses are looking for significant capital to expand and scale, and they typically have demonstrated the ability to generate revenue, which makes them suitable for SBIC funding.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Businesses can raise capital using multiple tranches through SBA SBIC services. This approach provides flexibility for both the business and the investor, allowing funding to be structured over time based on the company’s growth and achievement of specific milestones. It’s a way for businesses to meet their evolving capital needs while providing investors with a structured, lower-risk investment approach.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Businesses can use funds obtained from SBA SBIC services for a wide range of purposes, including working capital, expansion, capital expenditures, acquisitions, R&D, and marketing. The specific use of funds will depend on the company's strategic goals and where it needs capital to drive growth and achieve its objectives. SBIC funding is flexible and can be tailored to the specific needs of businesses that are looking to expand, innovate, and scale their operations.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    To successfully raise capital through SBA SBIC services, a business needs a moderate to high risk tolerance. This is due to the combination of equity and debt financing, market challenges, and long-term growth goals involved in such funding. Ultimately, businesses seeking SBA SBIC funding should have a clear vision for growth, a solid business model, and the financial resilience to handle the complexities and risks that come with this type of capital.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    To apply for and benefit from SBA SBIC services, businesses should have a moderate to high capital cost tolerance. They need to be prepared for ownership dilution, debt service costs, transaction costs, repayment obligations and the potential need for multiple funding rounds which could involve further costs.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    While the specific costs will depend on the size of the deal and the complexity of the business, an average company seeking SBA SBIC funding can generally expect to incur $20,000 to $100,000 in upfront costs. This could be higher for larger, more complex deals, particularly when more specialized legal, financial, or accounting services are required. Businesses will need to consider legal fees, financial advisory fees, due diligence costs, and transaction fees. 
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    On average, businesses can expect to receive capital from SBA SBIC services in 3 to 6 months after the initial inquiry. Businesses should be prepared for a thorough due diligence process, multiple rounds of negotiations, and careful review of financials and operations, all of which can take time.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)