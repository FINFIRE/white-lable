import api from './client';
import type { MatchData } from '../types/api';

export async function getMatchData(): Promise<MatchData> {
  const { data } = await api.get<MatchData>('match-data-json');
  return data;
}

export async function getMatchPDF(): Promise<Blob> {
  const { data } = await api.get<Blob>('match-letter-pdf', {
    responseType: 'blob',
  });
  return data;
}
