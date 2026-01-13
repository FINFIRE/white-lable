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


def investmentbanking(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><b><u>Definition of Capital Market: Investment Banking</b></u><br></p>
    
    <p><b><u>Introduction</u></b><br>
    Investment banking is ideal for companies seeking to raise large-scale capital, execute mergers and acquisitions, or access public markets through IPOs. It is designed for companies that are mature or scaling rapidly and require sophisticated financial structuring, underwriting services, or strategic advisory to optimize valuation and growth. {n} fits this profile. Investment banking has long been a cornerstone of global corporate finance, helping enterprises navigate complex capital markets and strategic transitions. For example, in the first half of 2024, global investment banking revenues reached over $48 billion, with equity capital markets and M&A advisory accounting for a significant share. In 2023 alone, over $200 billion was raised through equity and debt offerings facilitated by investment banks. The average IPO deal size that year exceeded $300 million, showcasing the scale and impact of this financing method. While investment banking provides access to vast pools of institutional capital and strategic expertise, companies must also be aware of the significant costs, regulatory complexity, and intense due diligence involved in the process.  There are five types of Investment Bankings that we can match you with: 1) Broker Dealer Represented Investment Banking 2) Broker Syndication, 3) Equity Sale, 4) Investment Banker Debt, 5) Mezzanine Financing. We will select the most appropriate type of Investment Banking as per your business need.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1. Investment banking is a specialized segment of the financial services industry that helps companies raise capital by acting as intermediaries between businesses and investors. For companies looking to grow, investment banks provide services such as underwriting new debt or equity securities, facilitating mergers and acquisitions (M&A), and offering strategic advisory on financial transactions. These institutions help structure deals, price offerings, prepare investor materials, and manage regulatory filings—making them an essential partner for businesses seeking large-scale funding through public markets or private placements. (Kagan, 2024)
<br>
    <br>2. Investment banking offers several specialized avenues for companies to raise capital, each tailored to different stages of growth and financial goals. Equity financing is a common method, where investment banks help companies raise funds by issuing shares through Initial Public Offerings (IPOs) or private placements. For businesses not ready to go public, private equity placements allow them to secure investments from institutional or accredited investors. Debt financing is another route, in which investment banks structure and underwrite corporate bond offerings or syndicated loans, enabling companies to access large amounts of capital without giving up equity. In some cases, convertible debt instruments—a hybrid of equity and debt—are used to attract investors seeking lower risk with potential upside. Additionally, investment banks often assist with mergers and acquisitions (M&A), helping companies grow or restructure through strategic partnerships, while also raising capital as part of the deal structure. (Tamplin, 2023)
<br>
    <br>3. The history of investment banking dates back to the late 17th and early 18th centuries, with its roots in European merchant banking. However, modern investment banking took shape in the United States during the 19th century, driven by the need to finance massive infrastructure projects like railroads and industrial expansion. Firms such as J.P. Morgan & Co. became early pioneers, helping companies raise capital through bond issuances and equity offerings. The Glass-Steagall Act of 1933 later separated commercial and investment banking, reshaping the industry until its repeal in 1999 allowed large financial institutions to once again operate across both sectors. Over time, investment banks have evolved into global powerhouses offering a range of services, including mergers and acquisitions advisory, securities underwriting, and asset management—becoming integral to corporate finance and capital markets around the world. (History of Investment Banking, 2023)
<br>
    <br>4. Investment banking can be a powerful tool for companies seeking to raise capital, but it also comes with several risks that businesses should carefully consider. One primary risk is the potential loss of control—particularly when issuing equity, as it often involves diluting ownership and decision-making power. Additionally, the costs associated with investment banking services can be significant, including underwriting fees, legal expenses, and regulatory compliance costs. Timing is another factor; if the market conditions are unfavorable, a public offering or large capital raise could underperform, affecting the company’s valuation and investor perception. There’s also reputational risk—any misstep during due diligence or disclosure can damage the company’s image. Lastly, regulatory scrutiny is higher when working with investment banks, especially in public markets, which can increase administrative burdens and legal exposure. (Bsmart, 2024)
<br>
    <br>5. To successfully raise capital through investment banking, a company needs several key elements in place. First, it should have a well-established business model with a clear financial history, as investment banks typically require financial statements, projections, and other documents to assess the company’s performance and growth potential. Additionally, the company must have a solid understanding of its funding needs and how much capital it aims to raise. The business should also be prepared to undergo a due diligence process, where investment bankers will thoroughly evaluate the company’s operations, management, financials, and legal standing. Furthermore, companies need to be open to complying with regulatory requirements, including disclosures and filings mandated by securities authorities. Lastly, the company must have the capacity to manage the costs associated with investment banking services, which may include underwriting fees, legal expenses, and other related costs. A clear vision for using the raised capital and strategic plans for growth will further help in attracting investment bankers and investors. (Analytics, 2024)
    </p>
                             
    <p><b><u>References</u></b><br>
    <br>Kagan, J. (2024, August 6). Investment Banking: What it is and what investment bankers do. Investopedia. <a href="https://www.investopedia.com/terms/i/investment-banking.asp">https://www.investopedia.com/terms/i/investment-banking.asp</a>
<br>
    <br>Tamplin, T., & Tamplin, T. (2023, August 9). Investment Banking | Definition, Services, Types, & Example. Finance Strategists. <a href="https://www.financestrategists.com/banking/investment-banking/">https://www.financestrategists.com/banking/investment-banking/</a>
<br>
    <br>History of Investment Banking | Brief background. (2023, June 8). Wall Street Prep. <a href="https://www.wallstreetprep.com/knowledge/the-history-of-investment-banking/">https://www.wallstreetprep.com/knowledge/the-history-of-investment-banking/</a>
<br>
    <br>Bsmart_Gp0mu. (2024, October 14). Risks and Rewards of Investment Banking | BSMART. BSMART. <a href="https://www.bsmartpartners.com/blog/understanding-the-risks-and-rewards-of-investment-banking/?">https://www.bsmartpartners.com/blog/understanding-the-risks-and-rewards-of-investment-banking/?</a>
<br>
    <br>Analytics, & Analytics. (2024, July 16). Investment banking and raising capital for a company | CapCompass. CapCompass |. <a href="https://capcompasspartners.com/investment-banking-and-raising-capital-for-a-company/">https://capcompasspartners.com/investment-banking-and-raising-capital-for-a-company/</a>
    </p>
                             
    <p><b><u>Qualification Requirements</u></b>
    <br>• Legal Entity Structure: Must be a registered business entity (e.g., C-Corp, LLC).
    <br>• Compliance with Securities Laws: Adhere to SEC or relevant regulatory bodies’ securities regulations.
    <br>• Corporate Governance: Proper leadership with authority to make fundraising decisions.
    <br>• Financial Audits: Audited financial statements (typically for the past 3 years).
    <br>• Disclosure Requirements: Full disclosure of financial health, risks, and material changes.
    <br>• Investor Accreditation: Ensure investors meet accredited investor criteria for private placements.
    <br>• Compliance with Offering Regulations: Follow laws governing securities offerings (e.g., Securities Act of 1933, Reg D, Reg A).
    <br>• Contracts and Agreements: Formal agreements with the investment bank, underwriters, and legal counsel.
    <br>• Due Diligence and Legal Review: Cooperate with due diligence and ensure accuracy in legal and financial matters.
    <br>• Ongoing Reporting Requirements: Comply with ongoing legal reporting and disclosure obligations post-funding.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Plan: A comprehensive plan outlining the company’s mission, vision, market analysis, and growth strategies.
    <br>• Financial Statements: Historical financial statements (usually 3 years) including income statements, balance sheets, and cash flow statements.
    <br>• Financial Projections: Forecasted financial statements for the next 3-5 years, including projected income, expenses, and cash flow.
    <br>• Corporate Governance Documents: Board of directors’ meeting minutes, bylaws, and shareholder agreements.
    <br>• Capitalization Table: A detailed breakdown of the company’s ownership structure, including shares, options, and convertible securities.
    <br>• Legal Documents: Articles of incorporation, operating agreements, intellectual property rights, and any contracts or agreements relevant to the business.
    <br>• Due Diligence Materials: Any documents related to legal, regulatory, or financial due diligence, such as material contracts, licenses, and permits.
    <br>• Investor Presentation or Pitch Deck: A document or slide deck summarizing the company’s business model, financials, market opportunity, and funding needs.
    <br>• Use of Proceeds Statement: A clear explanation of how the raised funds will be used, including expansion, R&D, or debt repayment.
    <br>• Regulatory Filings: Any necessary filings with regulators, including SEC forms (e.g., S-1, Form D) or other required documents based on the funding structure.
    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def investmentbankingfaq(request):
    introduction = mark_safe("""                       
    <p><b><u>FAQs</u></b></p>
                             
    <p><b><u>1. What is investment banking?</u></b><br>
    • Answer: Investment banking is a division of banking that deals with raising capital for companies, governments, and other entities. It involves services like underwriting, facilitating mergers and acquisitions (M&A), issuing securities, and providing advisory services on complex financial transactions.
    </p>
                             
    <p><b><u>2. How do investment banks raise capital for companies?</u></b><br>
    • Answer: Investment banks help companies raise capital by either issuing stocks (equity financing) or bonds (debt financing). They assess the company’s needs, prepare the necessary documentation (such as prospectuses or private placement memorandums), and then sell the securities to institutional or retail investors.
    </p>
                             
    <p><b><u>3. What is the difference between investment banking and commercial banking?</u></b><br>
    • Answer: Commercial banking deals with traditional banking services like deposit-taking, loans, and basic financial products, while investment banking focuses on larger financial transactions such as raising capital, trading securities, and advising on M&A deals. Investment banks typically work with large companies, institutions, and governments.
    </p>
                             
    <p><b><u>4. What are the typical fees charged by investment banks?</u></b><br>
    • Answer: Investment banks generally charge underwriting fees, which can range from 5% to 7% of the capital raised. Additionally, there are fees for advisory services, legal expenses, and due diligence, which can add up to significant costs depending on the complexity of the deal.
    </p>
                             
    <p><b><u>5. What is an initial public offering (IPO), and how do investment banks help with it?</u></b><br>
    • Answer: An IPO is the process by which a private company offers shares to the public for the first time. Investment banks assist with an IPO by helping the company prepare, underwriting the offering, marketing the shares, and guiding the company through regulatory requirements. They also price the offering based on market conditions and demand.
    </p>
                             
    <p><b><u>6. Can small companies use investment banking services?</u></b><br>
    • Answer: Small companies may not typically work with major investment banks for large capital raises due to high fees and the complexity of the services provided. However, smaller companies can use boutique investment banks or advisory firms for services like raising capital, facilitating mergers, or getting strategic financial advice.
    </p>
                             
    <p><b><u>7. What is a private placement?</u></b><br>
    • Answer: A private placement involves selling securities directly to a small group of investors rather than through a public offering. Investment banks often facilitate private placements, which are faster and less costly than public offerings, but they may require a more selective group of institutional investors.
    </p>
                             
    <p><b><u>8. What is a merger and acquisition (M&A), and how do investment banks assist?</u></b><br>
    • Answer: M&A refers to the process of one company acquiring another or merging with it. Investment banks play a crucial role by advising on the strategy, negotiating the terms, assessing the value, and structuring the deal. They also help raise capital if needed for the transaction.
    </p>
                             
    <p><b><u>9. What is due diligence in investment banking?</u></b><br>
    • Answer:Due diligence is the investigation and verification process that investment banks conduct to assess the financial health, legal compliance, and market position of a company. It is an essential step in any major transaction, such as an IPO, private placement, or M&A.</p>
                             
    <p><b><u>10. What are the risks of working with an investment bank?</u></b><br>
    • Answer: The main risks include high fees, potential conflicts of interest, and market volatility. If the company does not meet its fundraising goals or if market conditions worsen, it may not secure the desired capital. Additionally, the lengthy and expensive process of preparing for an IPO or other transaction may not always lead to a successful outcome.</p>

    <p><b><u>11. How long does it take to raise capital through investment banking?</u></b><br>
    • Answer: The timeline can vary significantly depending on the type of capital being raised. For an IPO, it can take anywhere from six months to a year to prepare and launch. Private placements or smaller debt offerings may take less time, but complex M&A deals could take months or longer to finalize.</p>

    <p><b><u>12. Why do companies need investment banks?</u></b><br>
    • Answer: Investment banks provide expertise and resources that help companies navigate complex financial markets, raise significant capital, and execute large-scale transactions like mergers and acquisitions. Their role is critical in providing financial advisory services, managing risk, and ensuring compliance with regulatory standards.</p>                                            
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def investmentbankingtwelve(request):
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
    
    premarketStr = ''

    #Up front Cost options
    up_front_cost_options ={
        'Minimum $0 - Maximum $499' : 'this model remains financially inefficient as more upfront cost might be required for making deals with investment banking.',
        'Minimum $500 - Maximum $999' :  'this model remains financially inefficient as more upfront cost might be required for making deals with investment banking.',
        'Minimum $1000 - Maximum $2499' :  'this model remains financially inefficient as more upfront cost might be required for making deals with investment banking.',
        'Minimum $2500 - Maximum $4999' :  'this model remains financially inefficient as more upfront cost might be required for making deals with investment banking.',
        'Minimum $5000 - Maximum $9999' :  'this model remains financially inefficient as more upfront cost might be required for making deals with investment banking.',
        'Minimum $10000 - Maximum $24999' : 'this model remains financially inefficient as more upfront cost might be required for making deals with investment banking.',
        'Minimum $25000 - Maximum $49999' : 'it should ensure alignment between internal financial readiness and banker engagement timelines to avoid friction during investor outreach.',
        'More than $50000+' : 'it should ensure alignment between internal financial readiness and banker engagement timelines to avoid friction during investor outreach.',             
    }
    costanalysis = up_front_cost_options[upfrontcost]

    #Up front Cost options
    up_front_time_options ={
        '1 Day to 1 Week' : 'required time 1 day to 1 week is not a direct match with this capital market option.',
        '1 Week to 2 Week' : 'required time 1 week to 2 week is not a direct match with this capital market option.',
        '2 Weeks to 4 Weeks' : 'required time 2 weeks to 4 weeks is not a direct match with this capital market option.',
        '1 Month to 2 Months' : 'required time 1 month to 2 months is not a direct match with this capital market option.',
        '2 Months to 3 Months' : 'required time 2 months to 3 months matches with this option however depending upon the market scenario and internal documents prepared, the time might not be sufficient.',
        '3 Months to 6 Months' : 'required time 3 months to 6 months matches with this option.',
        '6 Months to 12 Months' : 'required time 6 months to 12 months matches with this option.',
        'More than 1 year' : 'required time More than 1 year matches with this option.',             
    }
    timeanalysis = up_front_time_options[upfronttime]

    for num,item in enumerate(premarket):
        if num == 0:
            premarketStr = premarketStr + str(item).lower()
        elif num == (len(premarket)-1):
                premarketStr = premarketStr +', and ' + str(item).lower()
        else:        
            premarketStr = premarketStr +', ' + str(item).lower()

    introduction = """
    <p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Investment Banking</p>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    As {n} enters a {stage}, engaging an investment bank can provide strategic capital solutions—ranging from equity raises to M&A advisory. This path is best suited for companies with solid financial performance, strong market positioning, and a compelling growth narrative. Investment banks can structure complex transactions to optimize valuation, timing, and investor alignment.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Investment banking services are generally accessible to {entity}. For {n} to qualify for institutional capital markets or strategic transaction support, its legal structure must support equity ownership transfer, issuance of preferred shares, or public company readiness. Clean corporate governance and audited financials are typically prerequisites.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    With {preraise} already secured in pre-capital, {n} demonstrates traction and institutional appeal—key signals for investment bankers evaluating potential transactions. This pre-capital base provides confidence to future investors and acquirers, reducing perceived risk and supporting premium valuation discussions.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    If {n}’s prior capital was raised through {premarketstr}; an investment banking partner can help structure the next capital event to minimize dilution, convert prior instruments efficiently, and align incentives across the capitalization table. This is particularly important in Series B/C rounds or strategic M&A scenarios.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    If {n} aims to raise {raisegoal} investment bankers can structure this as a single transaction or phased raise, using a mix of institutional investors, strategic partners, or family offices. They will evaluate revenue traction, TAM, EBITDA multiples, and growth comps to determine positioning. A robust use-of-funds narrative and a detailed financial model are essential to market readiness.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Investment banks specialize in leading growth equity, minority recapitalizations, and M&A transactions, often starting at capital raises of $10M or more. For {n}, advisory engagement may include investor targeting, deal structuring, term sheet negotiation, and managing the due diligence process—positioning the company for a value-maximizing transaction.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    While most investment banking-led raises are closed in single tranches, some may be structured with milestone-based follow-ons or dual-track options (e.g., raise now and consider M&A exit later). {n} should collaborate closely with its banker to align timing, valuation thresholds, and investor expectations across the funding lifecycle.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Capital raised through an investment banking process is commonly allocated to:
    <br>• Product development and team expansion
    <br>• Market expansion (domestic or international)
    <br>• Strategic acquisitions
    <br>• Restructuring or recapitalization
    <br>• Preparation for IPO or exit

    <br>Clear deployment strategy, ROI analysis, and growth milestones must be well-articulated in the investor materials.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Engaging with an investment bank introduces market timing risk, valuation volatility, and execution risk. While there’s no debt obligation, outcomes are tied to investor appetite and macroeconomic factors. For {n}, this means ensuring a strong financial narrative, preparing for rigorous due diligence, and maintaining multiple pathways to liquidity or capital access if the primary raise stalls.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The cost of capital raised via investment banking services depends on the transaction type:
    <br>• Equity raises typically dilute 10–30% depending on round size and valuation.
    <br>• Advisory fees range from 2% to 7% of the capital raised or transaction value.
    <br>• Retainers may be required upfront, credited against success fees.
    <br>For {n}, this structure offers access to high-quality institutional capital and strategic deal structuring at a known cost relative to outcome.
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    Upfront costs may include:
    <br>• Legal and accounting fees ($25,000–$100,000+)
    <br>• Investment banking retainers ($10,000–$50,000/month)
    <br>• Data room and diligence prep costs
    <br>• Third-party valuation or audit costs (if needed)
    <br>On an average upfront cost for investment banking might fall between $20,000 to $75,000.

    <br>If {n} has a {upfrontcost} allocated, {costanalysis}
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    <br>Investment banking-led transactions typically close in 2 to 6 months, depending on:
    <br>• Market conditions
    <br>• Company preparedness
    <br>• Investor appetite
    <br>• Regulatory or legal complexity
    <br>{n} Company can streamline the process by preparing:
    <br>• Audited financials
    <br>• A detailed investor deck and financial model
    <br>• A clear data room with all required documentation
    <br>• A cohesive management story and growth plan
    <br>Experienced advisory support can shorten execution time, maximize valuation, and drive competitive interest.
    <br> {timeanalysis}
    </p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime,premarketstr=premarketStr,timeanalysis=timeanalysis,costanalysis=costanalysis))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)