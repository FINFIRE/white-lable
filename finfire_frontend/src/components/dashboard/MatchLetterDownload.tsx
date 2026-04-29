import { getMatchPDF } from '../../api/match';

export async function downloadMatchPDF() {
  const blob = await getMatchPDF();
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'match-letter.pdf';
  a.click();
  URL.revokeObjectURL(url);
}

export async function printMatchPDF() {
  const blob = await getMatchPDF();
  const url = URL.createObjectURL(blob);
  const win = window.open(url, '_blank');
  win?.addEventListener('load', () => win.print());
}
